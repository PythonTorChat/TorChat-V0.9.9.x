# -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2014-2019  M. Weigand       <doctortor@use.startmail.com>    #
#                                                                            #
# This program is licensed under the GNU General Public License V3,          #
# the full source code is included in the binary distribution.               #
#                                                                            #
# Included in the distribution are files from other open source projects:    #
# - TOR Onion Router (c) The Tor Project, 3-clause-BSD                       #
# - SocksiPy (c) Dan Haim, BSD Style License                                 #
# - Gajim buddy status icons (c) The Gajim Team, GNU GPL                     #
#                                                                            #
##############################################################################

import sys, os
#import locale
import numbers
import ConfigParser
import config
#import traceback
#import inspect
#import translations
#import shutil
#
# First Section is buddycount with single field with the count
#
BUDDYCOUNT = "0_TorChat"	   # Section Name
BCOUNT = "BuddyCount"        # Number buddies
#
# Next section is the buddylist with the buddies in display order. "000000" is myself and is never moved.
#    Buddies are listed with a 6 digit numeric ID that mirrors the position in the display list
#
BUDDYLIST = "1_BuddyList"    # List of buddies HS id's by number. This is where position in display list is managed
# 000000-999999 (artifical limit of 1,000,000 buddies)
#
# Next is sections by buddy with the HS address as the Section ID.
#
BUDDYADDR = "HSAddress"      # Buddy's Hidden Service Address aka OnionChat ID / address
BUDDYDNAME = "DisplayName"   # Either Profile name -or- override from user edit
BUDDYNOTES = "BuddyNotes"    # User entered notes
BUDDYPNAME = "ProfileName"   # Transmitted Profile name
BUDDYDECOR = "ProfileDecor"  # Transmitted Profile decoration
BUDDYCLIENT = "ChatClient"   # Transmitted Chat Client 
BUDDYVERSION = "ChatVersion" # Transmitted Chat Client Version
BUDDYPTEXT = "ProfileText"   # Transmitted Profile Text
BUDDYSTATUS = "ChatStatus"   # Available or XA (Extended Away) - Available, follows user status, XA always sends XA
BUDDYMASK = "ActionMask"     # Features enable / disable (xmit files allowed, etc.)
BUDDYHPOS = "ChatWinHPos"    # Saved Chat window Horizontal position
BUDDYVPOS = "ChatWinVPos"    # Saved Chat window Vertical position
BUDDYWSIZE = "ChatWinWSize"  # Saved Chat window Window "Sash" size
BUDDYHSIZE = "ChatWinHSize"  # Saved Chat window horizontal size
BUDDYVSIZE = "ChatWinVSize"  # Saved Chat window vertical size

def isWindows():
    return sys.platform.startswith("win")

#if isWindows():
#    import ctypes

bconfig_defaults = {
    (BUDDYCOUNT, BCOUNT) : 0
}

def getBuddyName(address):
    bname=get(address, BUDDYDNAME)
    if bname == "":
        return address
    else:
        return bname

def findex(index):
    if isinstance(index, numbers.Number):
        return '%(count)06d' % {'count': index}
    else:
        return '999999'


class OrderedRawBConfigParser(ConfigParser.RawConfigParser):
    def __init__(self, defaults = None):
        ConfigParser.RawConfigParser.__init__(self, defaults = None)

    def write(self, fp):
        """Write an .ini-format representation of the configuration state."""
        if self._defaults:
            fp.write("[%s]\n" % ConfigParser.DEFAULTSECT)
            for key in sorted(self._defaults):
                fp.write( "%s = %s\n" % (key, str(self._defaults[key]).replace('\n', '\n\t')))
            fp.write("\n")
        for section in sorted(self._sections):
            fp.write("[%s]\n" % section)
            for key in sorted(self._sections[section]):
                if key != "__name__":
                    fp.write("%s = %s\n" %
                             (key, str(self._sections[section][key]).replace('\n', '\n\t')))
            fp.write("\n")

def initBuddyConfig():
    global buddy_file_name
    global buddy_config
    bdir = config.getDataDir()
    if not os.path.isdir(bdir):
        os.mkdir(bdir)
    buddy_file_name = bdir + "/buddy-list.ini"
    buddy_config = OrderedRawBConfigParser()

def readConfig():
    #remove the BOM (notepad saves with BOM)
    if os.path.exists(buddy_file_name):
        f = file(buddy_file_name,'r+b')
        try:
            header = f.read(3)
            if header == "\xef\xbb\xbf":
                print "found UTF8 BOM in buddy-list.ini, removing it"
                f.seek(0)
                f.write("\x20\x0d\x0a")
        except:
            pass
        f.close()

    try:
        buddy_config.read(buddy_file_name)
    except ConfigParser.MissingSectionHeaderError:
        print ""
        print "*** buddy-list.ini must be saved as UTF-8 ***"
        sys.exit()

    #try to read all known options once. This will add
    #all the missing options to the config file (kindof a moot point here, but just in case new ones are added)
    for section, option in bconfig_defaults:
        get(section, option)

def writeConfig():
    fp = open(buddy_file_name, "w")
    os.chmod(buddy_file_name, 0600)
    buddy_config.write(fp)
    fp.close()

def get(section, option):
    if not buddy_config.has_section(section):
        buddy_config.add_section(section)
    if not buddy_config.has_option(section, option):
        value = bconfig_defaults[section, option]
        bset(section, option, value)
    value = buddy_config.get(section, option)
    if type(value) == str:
        try:
            value = value.decode("UTF-8")
            value = value.rstrip(" \"'").lstrip(" \"'")
        except:
            print "***  file buddy-list.ini is not UTF-8    ***"
            print "*** this will most likely break things   ***"
    elif type(value) == int:
        value = str(value)
    elif type(value) == float:
        value = str(value)

    return value # this should now be a unicode string

def getWithDefault(section, option, defaultValue):
#MW - Use this one to activate some test-only options in the .ini file
#     supplied default will direct normal actions. Test framework code.
    if not buddy_config.has_section(section):
        return defaultValue
    if not buddy_config.has_option(section, option):
        return defaultValue
    value = buddy_config.get(section, option)
    if type(value) == str:
        try:
            value = value.decode("UTF-8")
            value = value.rstrip(" \"'").lstrip(" \"'")
            if value == "":
                return defaultValue
        except:
            print "***  file buddy-list.ini is not UTF-8    ***"
            print "*** this will most likely break things   ***"
    elif type(value) == int:
        value = str(value)
    elif type(value) == float:
        value = str(value)

    return value # this should now be a unicode string

def getint(section, option):
    value = get(section, option).lower()
    if value in ["yes", "on", "true"]:
        return 1
    if value in ["no", "off", "false"]:
        return 0
    try:
        return int(value)
    except:
        return 0

def bset(section, option, value):
    if not buddy_config.has_section(section):
        buddy_config.add_section(section)
    if type(value) == bool:
        value = int(value)
    if type(value) == unicode:
        value = value.encode("UTF-8")
    buddy_config.set(section, option, value)
    writeConfig()

def b_del_section(section):
    if  buddy_config.has_section(section):
        return buddy_config.remove_section(section)
    return False

def b_del_option(section, option):
    if  buddy_config.has_option(section, option):
        return buddy_config.remove_option(section, option)
    return False
    
