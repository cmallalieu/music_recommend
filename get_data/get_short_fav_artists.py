import spotipy


def get_short_fav_artists(token):

    sp = spotipy.Spotify(auth=token)

    # get top 20 artists from 'short_term' time frame
    artists_0_19 = sp.current_user_top_artists(limit=20, offset=0, time_range='short_term')


    full_artist_list = []

    # aggregate all top artists into a single list to return
    for i in range(20):
        if i < 20:
            full_artist_list.append(artists_0_19['items'][i % 20]['name'])
    return full_artist_list

