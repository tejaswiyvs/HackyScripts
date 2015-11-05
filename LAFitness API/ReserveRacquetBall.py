import urllib2
import urllib

def get_timeslots(day):
	"""Accepts a day and returns the available racquetball court timeslots for that day."""
	headers = {}
	headers["Content-Type"] = 'application/json; charset=utf8'
	headers["Authorization"] = 'Basic <snip>' # Insert AuthKey here.
	data = read_json_file('./GetAmenityAvailability.txt')
	data = urllib.urlencode(data)
	req = urllib2.Request('https://api.lafitness.com/Services/Private.svc/GetAmenityAvailability', data=data, headers=headers)
	return urllib2.urlopen(req).read()


def read_json_file(file_path):
	f = open(file_path)
	return f.read()


if __name__ == '__main__':
	get_timeslots(1)
