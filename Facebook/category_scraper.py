import facebook

facebook = facebook.GraphAPI(access_token='AAACEdEose0cBALXwsHPPbqbn1JO9OEbVEXaBbvZCZCDMDR4yJszSIFvz0iGS7FUUqmzc3Kh2WTztoXtppkaQ2eEHYhyWVw9n1jUb6lMAZDZD')
facebook.api_key = 250994151631017
coordinates = ['', '', '', '', '', '', '']
categories = {}
args = {}
args["type"] = "place"
args["limit"] = 1000
args["center"] = "40.717209,-74.006335"
args["fields"] = "id,category"
result = facebook.request('/search', args)
f = open('./fb_pages.dat', 'w')
for dict in result["data"]:
	category_arr = facebook.fql('SELECT categories FROM page WHERE page_id = \''+dict["id"]+'\'')
	pages[dict["id"]] = []
	pages[dict["id"]].append(dict["category"])
	for dict2 in category_arr[0]['categories']:
		pages[dict["id"]].append(dict2["name"])
print pages

100383549148
Restaurant/cafe
French Restaurant / Fine Dining Restaurant