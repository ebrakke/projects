import httplib, json
import sys, os, time, zipfile
import logging
import utils

from urlparse import urljoin


#Set home path to be one above the '/src'
HOME_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BASE_URL = utils.BASE_URL


def getPage(entity, parent='', file_type='json', verbose=utils.verbose):

	if entity not in os.listdir(os.path.join(HOME_DIR, parent)):
		os.mkdir(os.path.join(HOME_DIR ,parent, entity))  #Create and entity folder if one does not exists

	#Check for the expected file type	
	if file_type =='json':

		if 'json' not in os.listdir(os.path.join(HOME_DIR, parent, entity)):
			os.mkdir(os.path.join(HOME_DIR, parent, entity, 'json'))  #Make a json folder in the entity if one does not exists
		entity_settings = utils.getSettings(entity)  
		query_info = entity_settings.get('query_info')

		#Check the query type
		if query_info.get('type') == 'range':
			start,stop,increment = query_info.get('range_info')
			conn = httplib.HTTPConnection(BASE_URL)

			#Query and Increment step
			for i in range(start, stop, increment):		
				#try:
				args = {p:i for p in query_info.get('params')}
				time.sleep(utils.request_interval)
				url = '/%s%s?%s=%s' % (query_info.get('url_subpath'), query_info.get('extension'), query_info.get('params')[0], str(i))
				print url
				conn.request('GET', url)
				p = conn.getresponse().read()

				#Write the recieved json to a file 
				with open(os.path.join(HOME_DIR, parent, entity, 'json', '%s.json' % str(i)), 'w') as f:
					f.write(p)
					f.close()
				#except Exception, e:
				#	logging.warning(" There was an error: %s" % str(e))

		#Zip the files and remove the duplicates
		zipAndRemove(parent, entity)


def zipAndRemove(path, entity, file_type='json'):
	os.chdir(os.path.join(HOME_DIR, path,entity, file_type))

	#Zip all of the files
	archive = zipfile.ZipFile('crawing-%s.zip' % time.strftime('%d-%m-%y'), 'a') #Create the archive
	files = [f for f in os.listdir('.') if file_type in f]
	for f in files:
		archive.write(f)
	archive.close()

	#delete all of the duplicate files
	files = [f for f in os.listdir('.') if f.endswith(file_type)]
	for f in files:
		os.remove(f)


if __name__ == '__main__':

	if sys.argv[1] == '-getpage':
		getPage(sys.argv[2], sys.argv[3])
		
	