import facebook
import sys
import operator

def get_categories(auth_token, api_key, coordinates, limit=1000):
	fb = facebook.GraphAPI(auth_token)
	fb.api_key = api_key
	categories = {}
	args = {}
	args["type"] = "place"
	args["limit"] = 1000
	args["fields"] = "id"
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
	return categories

if __name__ == '__main__':
	if len(sys.argv) < 4:
		raise TypeError("Invalid # of args. Usage: auth_token, api_key, coordinate1, coordinate2 ...")
	categories = get_categories(auth_token=sys.argv[1], api_key=sys.argv[2], coordinates=sys.argv[3:len(sys.argv)])
	sorted_categories = sorted(categories.iteritems(), key=operator.itemgetter(1))
	f = open('./results.txt', 'w')
	for item in sorted_categories:
		f.write(str(item[0]) +'\t'+str(item[1])+'\n')
	f.close()