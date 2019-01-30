import os
import argparse
import pymysql

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--dbuser", required=True, type=str,
                    help="database user used to connect to nextcloud database")
parser.add_argument("-p", "--dbpassword", required=True, type=str,
                    help="password for database user used to connect to nextcloud database")
parser.add_argument("-d", "--db", required=True, type=str,
                    help="nextcloud database name")
parser.add_argument("-s", "--dbserver", required=True,
                    type=str, help="database server ip")
parser.add_argument("-o", "--outputfile", required=False,
                    type=str, help="path and file name of output file")
parser.add_argument("-b", "--unban", required=False,
                    type=str, help="ip address to unban")

args = parser.parse_args()

dbconnection = pymysql.connect(host=args.dbserver, user=args.dbuser,
                               password=args.dbpassword, db=args.db, cursorclass=pymysql.cursors.DictCursor)


path, filename = os.path.split(args.outputfile)

os.chdir(path)

bannedips = open(filename, 'w')

cursor = dbconnection.cursor()

cursor.execute("SELECT * FROM oc_bruteforce_attempts;")

results = cursor.fetchall()

iplist = set()

for i in results:
    if i['ip'] not in iplist:

        bannedips.write(i["ip"] + "\n")

        iplist.add(i["ip"])

bannedips.close()
