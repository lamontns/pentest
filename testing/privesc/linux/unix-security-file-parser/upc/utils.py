import wpc.conf
import re
import os


def get_banner():
    return "unix_security_file_parser v%s (http://pentestmonkey.net/unix_security_file_parser)\n" % get_version()


def print_banner():
    print get_banner()


def get_version():
    wpc.conf.version = "0.1"
    svnversion = "$Revision: 0 $"  # Don't change this line.  Auto-updated.
    svnnum = re.sub('[^0-9]', '', svnversion)
    if svnnum:
        wpc.conf.version = wpc.conf.version + "svn" + svnnum

    return wpc.conf.version


# Walk a directory tree, returning all matching files
#
# args:
#   dir         directory to descend
def dirwalk(directory):
    for root, dirs, files in os.walk(directory):
            for file in files:
                    yield os.path.join(root, file)

