NAME = "TorChat"
VERSION_MAIN = "0"
VERSION_MAJOR = "9"
VERSION_MINOR = "9"
VERSION_BUILD = 555
EXPERIMENTAL = False

# 
# source distribution is on git thus versions are manually incremented
# VERSION_BUILD after each official release.
# 

VERSION = VERSION_MAIN + "." + VERSION_MAJOR + "." + VERSION_MINOR + "." + str(VERSION_BUILD)
VERSION_ONLY = VERSION
if EXPERIMENTAL:
    VERSION += "-experimental"

