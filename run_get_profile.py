import spotipy
from get_data.get_auth import get_auth_token

def get_user_profile(username):

    # get auth token for username
    token = get_auth_token(username=username)

    # pass auth token to create spotipy object
    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        print('Error, cannot get authorization token')

    # get user profile information
    user_profile = sp.current_user()

    return user_profile
