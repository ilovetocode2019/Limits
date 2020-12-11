import collections

__version__ = "0.1.0a"

VersionInfo = collections.namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(major=0, minor=1, micro=1, releaselevel="final", serial=0)
