pkgname = "runc"
pkgver = "1.1.9"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["all", "man", f"COMMIT=chimera-r{pkgrel}"]
make_check_target = "localunittest"
hostmakedepends = [
    "bash",
    "gmake",
    "go",
    "go-md2man",
    "pkgconf",
]
makedepends = [
    "libseccomp-devel",
    "linux-headers",
]
pkgdesc = "CLI tool for spawning and running containers on Linux"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/opencontainers/runc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "509993674481aad7e14aedfb280e0eb160f3a34c0b77e2e98c4b3c0b1df76894"
# objcopy fails on ppc
# tests create namespaces and fail because no perms
options = ["!debug", "!check"]


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def do_install(self):
    # rather than patch -D, just copy the files
    self.install_file("runc", "usr/bin")
    self.install_files("man/man8", "usr/share/man")
