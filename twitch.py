import json, sys, getopt
import urllib.request as ulib

def fetch_kraken(TwitchChannel): # return the stream Id is streaming else returns -1
    clientid = 'taf50me5uagadpa70zl5rf8vp0j3d96'
    url = str('https://api.twitch.tv/kraken/streams/'+TwitchChannel+'?client_id='+clientid)
    try:
        response = ulib.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
    except:
        data = ""

    return data


def main(argv):
    helpstr = 'usage: twitch.py channel [-...] ...'

    try:
        opts, args = getopt.getopt(argv,"h", [])
    except getopt.GetoptError:
        print (helpstr)
        sys.exit(2)

    if len(args) == 1:
        channel = args[0]
    else:
        print(helpstr)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print(helpstr)
            sys.exit()

    kraken_data = fetch_kraken(channel)

    if kraken_data == "":
        print('could not fetch data for channel ' + channel)
        sys.exit(2)

    print(kraken_data['stream']['channel']['status'])


if __name__ == "__main__":
    main(sys.argv[1:]);
