########################################################################
#
#Json Linter Script
#
#Written By: Unni Krishnan J
#
#######################################################################
import fnmatch,os,json,logging, sys, datetime

matches = []

LOG_FILENAME = 'json.log'                                                #log file
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

error=0
dir_name = sys.argv[1]
now = datetime.datetime.now()

for root, dirnames, filenames in os.walk(dir_name):
    for filename in fnmatch.filter(filenames, '*.json'):                 #getting the names of all the json files
        matches.append(os.path.join(root, filename))
        pathname = root+ '/' + filename
        print pathname
        with open(pathname) as json_file:                                #json validations
             try:
                json_data = json.load(json_file)
             except ValueError, e:
             	print e
                logging.debug(now.strftime("%Y-%m-%d %H:%M")) 
                logging.debug(pathname)
                logging.debug(e)
                error +=1

if error == 0:
   print "All the json files are valid"
else:
   print "No Of Files with errors"
   print error

