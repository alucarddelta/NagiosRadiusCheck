# NagiosRadiusCheck

Python script that allows Nagios to report if a Radius server can be reached and communicated with.

Information is grabbed from a options.ini file that "currently" requires manual input.

The radius server IP must only be in the options.ini file.

# PING ONLY

Ping only only checks for ping requests being returned

# Master

When complete will check Ping and if a supplied Port, User, Pass and Secret are correct.
