from bottle import route, run, request
from AccessToken import GetAccessToken
from UserInfo import GetUserTopTracks, GetUsername
from csvconvert import csvconvert
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