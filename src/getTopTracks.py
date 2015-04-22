from config_lastfm import username, password, API_KEY, SECRET_KEY
import pylast

password_hash = pylast.md5(password)

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    SECRET_KEY, username = username, password_hash = password_hash)


def getArtist(artist):
    artistLastFm = network.get_artist(artist);
    return artistLastFm;

def getTopSongs(artist):
    toptracks = artist.get_top_tracks(limit=3)
    return toptracks;
    #===========================================================================
    # for track in toptracks:
    #     for i in track:
    #         songtitle = str(i)
    #===========================================================================

