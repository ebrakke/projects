import json

BASE_URL = r'www.reddit.com'
settings = json.loads(open('settings.json').read())

request_interval = settings.get('scrape_settings').get('request_interval')
verbose = settings.get('scrape_settings').get('verbose')



def traverseDict(d, keys):
	for k in keys:
		d = d.get(k)
	return d

def getSettings(entity):
	types = settings.get('entities')
	for t in types:
		if entity in t:
			return t.get(entity)