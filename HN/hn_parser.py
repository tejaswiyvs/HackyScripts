import json

f = open('hn.json', 'r')
results = json.loads(f.read())

print results['results'][0]['item']['id']