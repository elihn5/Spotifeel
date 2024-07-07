from bottle import route, run, request
from AccessToken import AccessToken
from UsertopTracks import UsertopTracks
from csvconvert import csvconvert
@route('/')
def index():
    print("activated")
    Oauth = request.query["code"]
    print(request.query["code"])
    Token = AccessToken(Oauth.strip())
    SongDict = UsertopTracks(Token)
    csvconvert(SongDict)
    print(SongDict)


run(host='localhost', port=8000)