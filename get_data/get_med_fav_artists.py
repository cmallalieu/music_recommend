import spotipy


def get_med_fav_artists(token):

    sp = spotipy.Spotify(auth=token)

    # get top 60 artists from 'medium_term' time frame
    artists_0_19 = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
    artists_20_39 = sp.current_user_top_artists(limit=20, offset=20, time_range='medium_term')
    artists_40_59 = sp.current_user_top_artists(limit=20, offset=40, time_range='medium_term')

    full_artist_list = []

    # aggregate all top artists into a single list to return
    for i in range(60):
        if i < 20:
            full_artist_list.append(artists_0_19['items'][i % 20]['name'])
        elif i < 40:
            full_artist_list.append(artists_20_39['items'][i % 20]['name'])
        elif i < 60:
            full_artist_list.append(artists_40_59['items'][i % 20]['name'])

    return full_artist_list

