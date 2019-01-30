import os
import argparse
import pymysql

# Initialize arparse
parser = argparse.ArgumentParser()

"""Argument Parser:
    --dbuser:  Database user, required
    --dbpassword:  Password for the db user, required
    --db:  Database to work on
    --dbserver:  Database server to connect to, required
    --outputfile:  File to ouput list to, optional
    --unban:  IP address to unban
"""

parser.add_argument("-u", "--dbuser", required=True, type=str,
                    help="database user used to connect to nextcloud database")

parser.add_argument("-p", "--dbpassword", required=True, type=str,
                    help="password for database user")

parser.add_argument("-d", "--db", required=True, type=str,
                    help="nextcloud database name")

parser.add_argument("-s", "--dbserver", required=True,
                    type=str, help="database server ip")

parser.add_argument("-o", "--outputfile", required=False,
                    type=str, help="path and file name of output file")

parser.add_argument("-b", "--unban", required=False,
                    type=str, help="ip address to unban")

# Assign arguments to args
args = parser.parse_args()

# Declare PyMySql database connection
dbconnection = pymysql.connect(host=args.dbserver, user=args.dbuser,
                               password=args.dbpassword, db=args.db,
                               cursorclass=pymysql.cursors.DictCursor)

# If there's an output file connect to database and pull IP address
if args.outputfile:

    # Split file name from pat
    path, filename = os.path.split(args.outputfile)

    # Change Directory to path
    os.chdir(path)

    # Open the file
    bannedips = open(filename, 'w')

    # Connect to database server
    cursor = dbconnection.cursor()

    # Execute the sql query
    cursor.execute("SELECT * FROM oc_bruteforce_attempts;")

    # Fetch all results
    results = cursor.fetchall()

    # Initialize the list of IP addresses
    iplist = set()

    # Remove duplicates and write them to a file
    for i in results:
        if i['ip'] not in iplist:

            bannedips.write(i["ip"] + "\n")

            iplist.add(i["ip"])

    bannedips.close()

else:

    # Connect to database server
    cursor = dbconnection.cursor()

    # Generate SQL command
    unbansql = "DELETE FROM oc_bruteforce_attempts WHERE ip = '" + args.unban + "';"

    # Prepare to execute the SQL command
    cursor.execute(unbansql)

    # Execute the command
    dbconnection.commit()

    #  Let the person know the IP was removed from the list
    print('Unbanned ip address ' + args.unban)
