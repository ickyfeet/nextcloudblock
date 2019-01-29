import os
import argparse
import pymysql

parser = argparse.ArgumentParser()

parser.add_argument("dbuser",type=str,help="database user used to connect to nextcloud database")
parser.add_argument("dbpassword",type=str,help="password for database user used to connect to nextcloud database")
parser.add_argument("db",type=str,help="nextcloud database name")
parser.add_argument("dbhost",type=str,help="database server ip")
parser.add_argument("outputfile",type=str,help="path and file name of output file")

args = parser.parse_args()

dbconnection = pymysql.connect(host=args.dbhost, user=args.dbuser, password=args.dbpassword, db=args.db, cursorclass=pymysql.cursors.DictCursor)


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
