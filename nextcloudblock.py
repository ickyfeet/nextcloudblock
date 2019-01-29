import os
import argparse
import pymysql

parser = argparse.ArgumentParser()

parser.add_argument("dbuser",type=str,help="database user used to connect to nextcloud database")
parser.add_argument("dbpassword",type=str,help="password for database user used to connect to nextcloud database")
parser.add_argument("dbhost",type=str,help="database server ip")
parser.add_argument("outputfile",type=str,help="path and file name of output file")
