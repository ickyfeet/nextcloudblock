# nextcloudblock

Allows you to manage the IP addresses banned by nextcloud


Requires PyMySql


Pass the following arguments at the command line:

* -u Database User *required*
* -p Database Password *required*
* -d Nextcloud Database *required*
* -s Nextcloud Server IP *required*
* -o File path and name to dump the ip addresses into
* -b IP address to unban
* -v View the list of banned IP addresses

Usage:  

* Write the list to a file
  * python3 nextcloudblock.py -u dbuser -p dbuserpassword -d databasename -s serverip -o /path/to/file.txt

* Unban IP address from list
  * python3 nextcloudblock.py -u dbuser -p dbuserpassword -d databasename -s serverip -b unbanip

* View list of banned IP addresses
  * python3 nextcloudblock.py -u dbuser -p dbuserpassword -d databasename -s serverip -v

