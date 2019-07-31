from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import configparser

def get_auth_token(username, scope='user-top-read', redirect_uri='http://localhost/'):
    # get hidden client id and client secret
    config = configparser.ConfigParser()
    config.read('./get_data/config.ini')
    client_id = config['DEFAULT']['client_id']
    client_secret = config['DEFAULT']['client_secret']

    # get token
    try:
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        return token
    except:
        return False
