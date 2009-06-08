#!/usr/bin/env python

import re
from optparse import OptionParser

def loc(contents):
    a = re.compile("(?i)<span class=\"adr\">[\w, -\.:]+</span>")
    loc = a.search(contents)
    if loc:
        location = contents[loc.start():loc.end()]
        return location[location.find(">")+1:location.rfind("<")]

def main():
    (options, args) = parser.parse_args()
  
    if options.v:
        print "verbose mode on"
    if options.f:
        if options.v:
            print "input file: ", options.f
        file = open(options.f,'r')
        contents = file.read()
        file.close()
        print "contents of file: ",contents
        print loc(contents)

parser = OptionParser()
parser.add_option("-v",
    "--verbose",
    action="store_true",
    dest="v",
    default=False,
    help="turn on verbose mode")
parser.add_option("-f",
    "--file",
    dest="f",
    metavar="FILE",
    help="name of input file to search")
        
if __name__ == "__main__":
    main()