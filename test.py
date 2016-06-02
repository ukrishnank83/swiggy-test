import fnmatch,os,json,logging, sys, datetime
matches = []
LOG_FILENAME = 'json.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

dir_name = sys.argv[1]
now = datetime.datetime.now()
for root, dirnames, filenames in os.walk(dir_name):
    for filename in fnmatch.filter(filenames, '*.json'):
        matches.append(os.path.join(root, filename))
        pathname = root+ '/' + filename
        print pathname
        with open(pathname) as json_file:
             try:
                json_data = json.load(json_file)
             except ValueError, e:
             	print e
                logging.debug(now.strftime("%Y-%m-%d %H:%M")) 
                logging.debug(pathname)
                logging.debug(e)
        
