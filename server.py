from bottle import route, run, request
from api.AccessToken import GetAccessToken
from api.UserInfo import GetUserTopTracks, GetUsername
from api.csvconvert import csvconvert
@route('/')
def index():
    print("activated")
    print(request.query)
    Oauth = request.query["code"]
    print(request.query["code"])
    Token = GetAccessToken(Oauth.strip())
    SongDict = GetUserTopTracks(Token)
    username = GetUsername(Token)
    csvconvert(SongDict, username)
    print(SongDict)


run(host='localhost', port=8000)