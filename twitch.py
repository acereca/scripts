import urllib2, json, sys

def IsTwitchLive(TwitchChannel): # return the stream Id is streaming else returns -1
    url = str('https://api.twitch.tv/kraken/streams/'+TwitchChannel)
    streamID = -1
    respose = urllib2.urlopen(url)
    html = respose.read()
    data = json.loads(html)
    try:
       streamID = data['stream']['_id']
    except:
       streamID = -1
    return int(streamID)


print(IsTwitchLive(sys.argv[1]))
