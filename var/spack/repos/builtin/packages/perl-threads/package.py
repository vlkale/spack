# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlThreads(PerlPackage):
    """threads - Perl interpreter-based threads"""

    homepage = "https://metacpan.org/pod/threads"
    url = "https://cpan.metacpan.org/authors/id/J/JD/JDHEDDEN/threads-2.21.tar.gz"

    version("2.21", sha256="28394c98a2bcae6f20ffb8a3d965a1c194b764c650169e2050ee38dbaa10f110")
