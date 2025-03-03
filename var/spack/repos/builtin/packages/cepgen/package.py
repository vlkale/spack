# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cepgen(CMakePackage):
    """A generic central exclusive processes event generator"""

    homepage = "https://cepgen.hepforge.org/"
    url = "https://github.com/cepgen/cepgen/archive/refs/tags/1.0.2patch1.tar.gz"

    tags = ["hep"]

    license("GPL-3.0-or-later")

    version("1.2.5", sha256="5016c5a9b505035f849f47bdf35ecfb8c98d45dd1e086fae64f264a30adb120d")
    version("1.1.0", sha256="2a4eaed161f007269516cbfb6e90421e657ab1922d4509de0165f08dde91bf3d")
    version(
        "1.0.2patch1", sha256="333bba0cb1965a98dec127e00c150eab1a515cd348a90f7b1d66d5cd8d206d21"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    generator("ninja")

    depends_on("cmake@3.5:", type="build", when="@1.0:")
    depends_on("cmake@3.20:", type="build", when="@1.1:")

    depends_on("gsl")
    depends_on("openblas")
    depends_on("hepmc")
    depends_on("hepmc3")
    depends_on("lhapdf")
    depends_on("pythia6")
    depends_on("root")
