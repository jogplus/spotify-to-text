import json
import urllib.request
import urllib.parse
import base64

def generate_track_list(songs: list, track_list: list) -> list:
    '''Turns the list of addresses into a list of tuples that
    can be used by the url_build function'''
    songtxt = ''
    if len(songs) > 49:
        for song in songs[:49]:
            songtxt += song + ','
        songtxt = songtxt[:-1]
        url = url_build(songtxt)
        print('loading...')
        jason_text = url_load(url)
        track_list += print_jason(jason_text)
        return generate_track_list(songs[50:], track_list)
    else:
        for song in songs:
            songtxt += song + ','
        songtxt = songtxt[:-1]
        url = url_build(songtxt)
        jason_text = url_load(url)
        track_list += print_jason(jason_text)
        track_list.sort()
        print('done!')
        return track_list

def url_build(songtxt: list) -> list:
    '''Uses a list of tuples to create a direction api url'''
    url = 'https://api.spotify.com/v1/tracks?ids=' + songtxt
    return url

def url_load(url: str) -> dict:
    '''Takes a url, opens it, returns the json text within it,
     and then finally closes it'''
    client_id = 'd82d1ee7fe604b56ac800a4e9f8477e0'
    client_secret = '79689b652261464f8c718b4613369ab2'
    auth_req64 = base64.b64encode((client_id + ':' + client_secret).encode('UTF-8'))
    auth_req_url = 'https://accounts.spotify.com/api/token'
    data_encoded = urllib.parse.urlencode({'grant_type':'client_credentials'}).encode('UTF-8')
    token_header = {'Authorization':'Basic '+auth_req64.decode()}

    request_response = urllib.request.Request(auth_req_url, data_encoded, token_header)
    response = urllib.request.urlopen(request_response)
    access_token = json.load(response)['access_token']
    song_header = {'Authorization':'Bearer '+ access_token}

    request_response = urllib.request.Request(url, None, song_header)
    response = urllib.request.urlopen(request_response)
    jason_text = json.load(response)
    return jason_text

def print_jason(jason_text):
    track_list = []
    for track in jason_text['tracks']:
        track_list.append(track['artists'][0]['name'] + ', ' + track['name'])
    return track_list



