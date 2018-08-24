import radius
import os
import configparser

config = configparser.ConfigParser()

config.read(options.ini)
Hostn = config.()

def check_ping():
    hostname =
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "NOK"
    else:
        pingstatus = "NFAIL"
    return pingstatus
