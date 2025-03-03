# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Pandoramonitoring(CMakePackage):
    """ROOT-based Event Visualisation Environment for Pandora with
    tree-writing functionality"""

    url = "https://github.com/PandoraPFA/PandoraMonitoring/archive/v03-04-00.tar.gz"
    homepage = "https://github.com/PandoraPFA/PandoraMonitoring"
    git = "https://github.com/PandoraPFA/PandoraMonitoring.git"

    tags = ["hep"]

    maintainers("jmcarcell", "wdconinc")

    version("master", branch="master")
    version("3.5.0", sha256="274562abb7c797194634d5460a56227444a1de07a240c88ae35ca806abcbaf60")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("root@6.18.04: +x +opengl")
    depends_on("pandorasdk")

    # https://github.com/PandoraPFA/PandoraMonitoring/pull/13
    @when("@:3.6.0")
    def patch(self):
        filter_file(
            "TTreeWrapper::Branch<T>::~Branch<T>",
            "TTreeWrapper::Branch<T>::~Branch",
            "src/TTreeWrapper.cc",
        )

    def cmake_args(self):
        args = [
            self.define("CMAKE_MODULE_PATH", self.spec["pandorapfa"].prefix.cmakemodules),
            self.define("CMAKE_CXX_FLAGS", "-std=c++17"),
        ]
        return args

    def url_for_version(self, version):
        # contrary to iLCSoft packages, here the patch version is kept when 0
        base_url = self.url[: self.url.rfind("/")]
        major = str(version[0]).zfill(2)
        minor = str(version[1]).zfill(2)
        patch = str(version[2]).zfill(2)
        url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url
