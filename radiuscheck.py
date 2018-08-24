import radius
import os
import configparser
import sys

#Loads configuration
config = configparser.ConfigParser()

config.read(options.ini)
rip = config.()
rport =
rsecret =
ruser
rpass =

#Checks the Radius ping resonse. Critical (2) if fail.
def check_ping():
    response = os.system("ping -c 1 " + rip)
    if response == 0:
        pingstatus = "NOK"
    else:
        pingstatus = "NFAIL"
    return pingstatus

#Checks the Radius configuration. Critical (2) if fail.
def check_radius():
    #If Null is confugured on port bypass#
    return radiusstatus


######
#Main#
######

#If clear, OK (0). If Server details are left as Null, Warning (1).
if check_ping(pingstatus) = "NFAIL":
        print "Unable to reach radius server IP"
        sys.exit(2)
    else:
        if checkradius(radiusstatus) = "RCSUCCESS":
                print "Radius Server can be reached and Auth Successful"
                sys.exit(0)
        elif checkradius(radiusstatus) = "NULL":
                print "Radius server can be reached, but No Auth Configured"
                sys.exit(1)
        elif checkradius(radiusstatus) = "":
                print "Radius server can be reached, but No Auth Configured"
                sys.exit(1)
