# nextcloudblock

Pulls the banned IP list and writes them to a file


Requires PyMySql


Pass the following arguments at the command line:

* Database User
* Database Password
* Nextcloud Database
* Nextcloud Server IP
* File path and name to dump the ip addresses into

Usage:  python3 nextcloudblock.py dbuser dbpassword db serverip /path/to/file.txt

