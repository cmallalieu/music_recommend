# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import spotipy.util as util

scope = 'user-library-read'
username = 'ic2uyujb93pc2hj6hpfibmnkp'
client_id = '862cc968de3c42fd8df0637ef79a28f2'
client_secret = 'e9276b43b9f54575afd0639af38608dd'
redirect_uri = 'http://localhost/'
audio_tracks = 'https://open.spotify.com/album/4EK8gtQfdVsmDTji7gBFlz'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)


if len(sys.argv) > 1:
    song_str = sys.argv[1]
else:
    song_str = 'Cigarette Daydreams'

song_id = ['https://open.spotify.com/track/0hKRSZhUGEhKU6aNSPBACZ']


sp = spotipy.Spotify(auth=token)
result = sp.search(song_str)
# for res in result['tracks']['items']:
#     if res['name'] == 'Cigarette Daydreams':
        # print(f'Song Name: {res["name"]}')
        # print(f'Song Id: {res["id"]}')
        # print()
        # song_id.append(res['id'])
#    if res[i]['name'] == 'Cigarette Daydreams':
#        pprint.pprint(res[i]['id'])
    #    pprint.pprint(result[i]['items'][0]['name'])

#    if res['name'] == 'Cigarette Daydreams':
#        pprint.pprint(res['id'])

#results = sp.search(q=artist_name, limit=2)
#tids = []
# for i, t in enumerate(results['tracks']['items']):
#     print(' ', i, t['name'])
#     tids.append(t['uri'])

start = time.time()
features = sp.audio_features(song_id)
delta = time.time() - start
for feature in features:
    print(json.dumps(feature, indent=4))
    print()
    analysis = sp._get(feature['analysis_url'])
    print(json.dumps(analysis, indent=4))
    print()
print ("features retrieved in %.2f seconds" % (delta,))
