# NagiosRadiusCheck

Python script that allows Nagios to report if a Radius server can be reached and communicated with.

Information is grabbed from a options.ini file that "currently" requires manual input.

The radius server IP must only be in the options.ini file.

Details in "status information" and "Performance Data" will be updated in the Nagios fields. Status being a quick overview of the current status. Performance will be more detailed into what is currently occurring for troubleshooting.

# PING ONLY

Ping only only checks for ping requests being returned.

If a ping is successful, It will result in a OK status in Nagios. Performance data will be the ping result.
If a ping is unsuccessful, It will result in a CRITICAL status in Nagios. Performance data will be the ping result.

# Master

When complete will check Ping and if a supplied Port, User, Pass and Secret are correct.
