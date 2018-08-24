import radius
import os
import configparser
import sys

config = configparser.ConfigParser()

config.read(options.ini)
rip = config.()
rport =
rsecret =
ruser
rpass =

def check_ping():
    hostname =
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "NOK"
    else:
        pingstatus = "NFAIL"
    return pingstatus

if check_ping(pingstatus) = "NFAIL"
        print "Unable to reach radius server IP"
        sys.exit(1)
    elif
