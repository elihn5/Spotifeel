import requests
import base64
try: clientIDtext = open("../clientID.txt", "r+")
except FileNotFoundError:
		clientIDtext = open("../clientID.txt", "w+")
clientID = clientIDtext.read()
clientIDtext.close()

try: clientsecrettext = open("../clientSecret.txt", "r+")
except FileNotFoundError:
		clientsecrettext = open("../clientSecret.txt", "w+")
clientSecret = clientsecrettext.read()
clientsecrettext.close()

try: redirectURItext = open("../redirectURI.txt", "r+")
except FileNotFoundError:
		redirectURItext = open("../redirectURI.txt", "w+")
redirectURI = redirectURItext.read()
redirectURItext.close()
def GetAccessToken(OauthCode):
	client = clientID + ":" + clientSecret
	client_encode = client.encode('ascii')
	client_bytes = base64.b64encode(client_encode)
	client_base64 = client_bytes.decode('ascii')

	response = requests.post("https://accounts.spotify.com/api/token", data={
		"grant_type":"authorization_code",
		"code":OauthCode,
		"redirect_uri":redirectURI
		},
		headers={
			'Content-Type': 'application/x-www-form-urlencoded',
			'Authorization': "Basic " + client_base64
		}
		)
	print(response)
	print(response.json())
	return response.json()["access_token"]