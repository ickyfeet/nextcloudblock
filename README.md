# nextcloudblock

Pulls the banned IP list and writes them to a file


Requires PyMySql


Pass the following arguments at the command line:

* -u Database User *required*
* -p Database Password *required*
* -d Nextcloud Database *required*
* -s Nextcloud Server IP *required*
* -o File path and name to dump the ip addresses into
* -b IP address to unban

Usage:  

* Write the list to a file
  * python3 nextcloudblock.py -u dbuser -p dbuserpassword -d databasename -s serverip -o /path/to/file.txt

* Unban IP address from list
  * nextcloudblock.py -u dbuser -p dbuserpassword -d databasename -s serverip -b unbanip

