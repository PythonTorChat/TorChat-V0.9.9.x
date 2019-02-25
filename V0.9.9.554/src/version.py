NAME = "TorChat"
VERSION_MAJOR = "0.9.9"
VERSION_SVN = 554
EXPERIMENTAL = False

# 
# source distribution is on git thus versions are manually incremented
# VERSION_SVN after each official release.
# 

VERSION = VERSION_MAJOR + "." + str(VERSION_SVN)
VERSION_ONLY = VERSION
if EXPERIMENTAL:
    VERSION += "-experimental"

