import radius
import os

def check_ping():
    hostname =
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "NOK"
    else:
        pingstatus = "NFAIL"
    return pingstatus
