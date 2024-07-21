import csv
import datetime

def csvconvert(songdata, username):
	date = datetime.datetime.now().replace(microsecond=0).isoformat()
	with open(f"data/{username + date.replace(':','-')}.csv", 'w', newline='') as csvfile:
		# creating a csv dict writer object
		writer = csv.DictWriter(csvfile, fieldnames=["acousticness", "danceability", "energy", "liveness", "speechiness", "valence"])
		# writing headers (field names)
		writer.writeheader()
		# writing data rows
		writer.writerows(songdata)