import radius
from ConfigParser import SafeConfigParser
import os
import sys

#Loads configuration
config = SafeConfigParser()
config.read('options.ini')
rip = config.get('settings','Host')
rport = config.get('settings','Port')
rsecret = config.get('settings','Secret')
ruser= config.get('settings','User')
rpass = config.get('settings','Pass')

#Checks the Radius ping resonse. Critical (2) if fail.
def check_ping():
    response = os.system("ping -c 1 -t 2000 " + rip + " > /dev/null 2>&1")
    if response == 0:
        pingstatus = "NOK"
    else:
        pingstatus = "NFAIL"
    return pingstatus

#Checks the Radius configuration. Critical (2) if fail.
def check_radius():
    #If Null is confugured on port bypass#

#   radiusstatus = "NULL"
    return radiusstatus


######
#Main#
######

pingstatus = check_ping()
authradius = check_radius()

#If clear, OK (0). If Server details are left as Null, Warning (1).
if pingstatus == "NFAIL":
    print "Unable to reach radius server IP."
    sys.exit(2)

if authradius == "RCSUCCESS":
    print "Radius Server can be reached and Auth Successful."
    sys.exit(0)
elif authradius == "NULL":
    print "Radius server can be reached, but No Auth configured to test."
    sys.exit(1)
elif authradius == "RCFAIL":
    print "Radius server can be reached, No Auth Failed."
    sys.exit(2)
