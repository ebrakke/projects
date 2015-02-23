# Web scraping and parsing scripts

This is a small project of mine in which I wanted to experiment with scraping the web for data.  Currently, I am working on the scraping aspect of the project.

##Structure
*path/to/project-folder*

    logs/
	src/
	entity1/
	...
	...
    entity5/
    ...
    ...

##settings.json
This settings folder will tell `scraping_scrips.py` how to use `getPage()` to query a website.

First is the *scrape_settings* field.
**request_interval** is how much time will elapse in between each GET request
 **verbose** by default is set to false.  If you wish to have everything verbose, just turn this on

Next are the **entity** fields:

**query_info** will tell the program how to interact with the web
	`url_subpath` is the url path to the entity information
	`extension` is the kind of files the query will return (So far only json is handled)
	`type` is the type of search that will be executed (currently range is supported)
	`params` are the parameters that will follow the extension (only count is supported)
		`range_info` is a list of [start, stop, increment] for the range query
		

**json_info** will tell the parser which information for the json you wish to extract

**file_info** will tell the program file information

I am still playing around with the settings document.  This is just to figure out how to work with settings files

##scraping_scripts.py
This file contains the scripts for gather raw data from the web

**getpage**
Get page takes and inputs and `entity` and and optional `parent`.  

It will then look to the *settings.json* file for information on `entity`.  Next it will execute the query as specified in the settings file.  At this point I am using [reddit](www.reddit.com) as an example to build this so everything is set up to work with JSON files.  The query pattern also follows close to that of reddit.  I hope to make this more generalized soon.

Once the program connects to the website, It will execute the queries, read the response page, and then save it as a JSON file in the /json directory.  Finally, all of the files will be zipped the duplicates are removed.

##example
