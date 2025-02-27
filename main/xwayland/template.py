pkgname = "xwayland"
pkgver = "23.2.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dipv6=true",
    "-Dxcsecurity=true",
    "-Ddri3=true",
    "-Dglamor=true",
    "-Dxvfb=false",
    "-Dxdmcp=false",
    "-Dxwayland_ei=socket",
    "-Dxwayland_eglstream=false",
    "-Dxkb_dir=/usr/share/X11/xkb",
    "-Dxkb_output_dir=/var/lib/xkb",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libei-devel",
    "libxfont2-devel",
    "libxkbfile-devel",
    "libxshmfence-devel",
    "libxcb-devel",
    "libxcvt-devel",
    "wayland-devel",
    "wayland-protocols",
    "libtirpc-devel",
    "mesa-devel",
    "libepoxy-devel",
    "pixman-devel",
    "nettle-devel",
    "dbus-devel",
    "font-util-devel",
    "xorgproto",
    "xtrans",
]
# check if this needs to be updated when updating
depends = ["xserver-xorg-protocol>=20180227"]
pkgdesc = "Xwayland X server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/xserver/-/archive/{pkgname}-{pkgver}/xserver-{pkgname}-{pkgver}.tar.gz"
sha256 = "842cd6043f13e59390727418b238e509b8d4c37bc60702852e2c977f384bf218"
hardening = ["!cfi"]  # TODO
# needs xtest repository
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.rm(self.destdir / "usr/share/man/man1/Xserver.1")
    # provided by xserver-xorg-protocol
    self.rm(self.destdir / "usr/lib/xorg/protocol.txt")
