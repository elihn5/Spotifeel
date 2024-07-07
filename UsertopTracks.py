import requests
import csv

# INPUT: a user's OAuth key
# OUTPUT: the URIs of their top 25 songs over the last month
def UsertopTracks(AccessToken):
	# loading the API key from the API txt file
	APIText = open("APIKey.txt", "r+")
	APIKey = APIText.read()
	APIText.close()

	clientIDtext = open("clientID.txt", "r+")
	clientID = clientIDtext.read()
	clientIDtext.close()

	clientsecrettext = open("clientSecret.txt", "r+")
	clientSecret = clientsecrettext.read()
	clientsecrettext.close()

	# prompting spotify API for the track info
	response = requests.get(
		"https://api.spotify.com/v1/me/top/tracks?time-range=short_term&limit=25",
		headers={
			"Authorization": "Bearer " + AccessToken
		}
	)
	# initializing
	IDs = ""

	# normal loop that sifts through the track data and gets the URIs, puts them together in a list
	for item in response.json()["items"]:
		IDs += item["id"]
		IDs += ','
	IDs = IDs[:-1]

	AFResponse = requests.get(
		"https://api.spotify.com/v1/audio-features?ids=" + IDs,
		headers={
			"Authorization": "Bearer " + APIKey
		}
	)

	APIText = open("APIKey.txt", "w")
	# if the APIkey worked, APIkey.txt is updated with the working APIkey just in case
	# if the APIkey didnt work, spotify is polled for a new one, APIkey.txt is updated with the new one, and the request is sent again
	if AFResponse.status_code == 200:
		APIText.write(APIKey)
	else:
		print("else loop activated")
		APIResponse = requests.post(
			"https://accounts.spotify.com/api/token",
			headers={
				"Content-Type": "application/x-www-form-urlencoded"
			},
			data="grant_type=client_credentials&client_id=" + clientID + "&client_secret=" + clientSecret

		)
		APIKey = (APIResponse.json()['access_token'])
		AFResponse = requests.get(
			"https://api.spotify.com/v1/audio-features?ids=" + IDs,
			headers={
				"Authorization": "Bearer " + APIKey
			}
		)

		APIText.write(APIKey)
	APIText.close()

	DictList = []
	for song in AFResponse.json()["audio_features"]:
		song_dict = {
			"acousticness": song["acousticness"],
			"danceability": song["danceability"],
			"energy": song["energy"],
			"liveness": song["liveness"],
			"speechiness": song["speechiness"],
			"valence": song["valence"],
		}
		DictList.append(song_dict)
	return DictList