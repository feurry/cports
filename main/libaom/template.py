pkgname = "libaom"
pkgver = "3.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_TESTS=OFF",
    "-DENABLE_NASM=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "python",
    "nasm",
    "doxygen",
]
makedepends = ["linux-headers"]
pkgdesc = "Reference implementation of the AV1 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://aomedia.org"
source = [
    f"https://storage.googleapis.com/aom-releases/{pkgname}-{pkgver}.tar.gz"
]
sha256 = ["d1773bb6f050b430af47741306ac37a6aa2fec7364cb0dc27e3b1454a138934f"]
# requires a testdata download, tests take long
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
    "CXXFLAGS": ["-D_GNU_SOURCE"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}

match self.profile().arch:
    case "ppc64":
        configure_args += ["-DENABLE_VSX=0"]
    case "aarch64":
        # requires an explicit assembler
        configure_args += ["-DCMAKE_ASM_COMPILER=clang"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libaom-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libaom-progs")
def _progs(self):
    return self.default_progs()
