#!/usr/bin/python

import os
import sys
import shlex
import subprocess


filen = "/usr/lib/nagios/plugins/options.ini"

file = open(filen,'r')
rip = file.read()
file.close()

command = shlex.split("ping -c 1 " + rip)
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()

if process.poll() == 0:
        pingstatus = "PINGOK"
else:
        pingstatus = "PINGFAIL"

pingresult = output
authradius = "NULL"

if pingstatus == "PINGFAIL":
    print "CRITICAL - Unable to reach radius server. " + rip + "\n | " + pingresult
    sys.exit(2)

if authradius == "NULL":
    print "OK - Radius server can be reached. " + rip + "\n | " + pingresult
    sys.exit(0)
