from flask_spotify_auth import getAuth, refreshAuth, getToken
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

#CLIENT_ID = config['DEFAULT']['client_id']
CLIENT_ID = '98024be3f43d40aa82643d244f9a35c8'

#CLIENT_SECRET = config['DEFAULT']['client_secret']
CLIENT_SECRET = 'b131fc2d0a2c428490157eed5b39cd13'
#Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = "user-top-read"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown 
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))
 
def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA