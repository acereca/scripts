import json, sys
import urllib.request as ulib

def IsTwitchLive(TwitchChannel): # return the stream Id is streaming else returns -1
    clientid = 'taf50me5uagadpa70zl5rf8vp0j3d96'
    url = str('https://api.twitch.tv/kraken/streams/'+TwitchChannel+'?client_id='+clientid)
    streamID = -1
    respose = ulib.urlopen(url)
    html = respose.read()
    data = json.loads(html)
    try:
       streamID = data['stream']['_id']
    except:
       streamID = -1
    return int(streamID)


print(IsTwitchLive(sys.argv[1]))
