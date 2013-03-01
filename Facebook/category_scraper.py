import facebook
import sys
import operator

def get_categories(auth_token, api_key, coordinates, limit=1000):
	fb = facebook.GraphAPI(auth_token)
	fb.api_key = api_key
	categories = load_from_file()
	args = {}
	args["type"] = "place"
	args["limit"] = limit
	args["fields"] = "id"
	try:
		for coordinate in coordinates:
			args["center"] = coordinate
			result = fb.request('/search', args)
			for dict in result["data"]:
				category_arr = fb.fql('SELECT categories FROM page WHERE page_id = \''+dict["id"]+'\'')
				for dict2 in category_arr[0]['categories']:
					if dict2["name"] not in categories:
						categories[dict2["name"]] = 1
					else:
						categories[dict2["name"]] = categories[dict2["name"]] + 1
	except:
		print 'Exception. Returning categories that have been completed.' + str(sys.exc_info()[0])
	return categories

def load_from_file():
	"""Reads results.txt and loads any existing categories"""
	try:
		f = open('./results.txt', 'r')
		categories = {}
		for line in f:
			components = line.split('\t')
			categories[components[0]] = int(components[1].strip())
		f.close()
		return categories
	except:
		return {}

if __name__ == '__main__':
	if len(sys.argv) < 4:
		raise TypeError("Invalid # of args. Usage: auth_token, api_key, coordinate1, coordinate2 ...")
	categories = get_categories(auth_token=sys.argv[1], api_key=sys.argv[2], coordinates=sys.argv[3:len(sys.argv)], limit=1000)
	sorted_categories = sorted(categories.iteritems(), key=operator.itemgetter(1))
	f = open('./results.txt', 'w')
	for item in sorted_categories:
		f.write(str(item[0]) +'\t'+str(item[1])+'\n')
	f.close()