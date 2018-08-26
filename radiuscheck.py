#!/usr/bin/python

import os
import sys
import shlex
import subprocess


filen = "/usr/lib/nagios/plugins/options.ini"

file = open(filen,'r')
rip = file.read()
file.close()

command = shlex.split("ping -c 1 -t 150 " + rip)
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()

if process.poll() == 0:
        pingstatus = "PINGOK"
else:
        pingstatus = "PINGFAIL"

pingresult = output
authradius = "NULL"

if pingstatus == "PINGFAIL":
    print "Unable to reach radius server IP.\n | " + pingresult
    sys.exit(2)

if authradius == "RCSUCCESS":
    print "Radius Server can be reached and Auth Successful."
    sys.exit(0)
elif authradius == "NULL":
    print "Radius server can be reached, but No Auth configured to test.\n | " + pingresult
    sys.exit(1)
elif authradius == "RCFAIL":
    print "Radius server can be reached, No Auth Failed."
    sys.exit(2)
