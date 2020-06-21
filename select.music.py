#! /usr/bin/env python3
import subprocess
import rofi

streamlist = []


class Stream(object):
    player = 'mpv'
    notify_cmd = 'dunstify'

    @staticmethod
    def notify(msg: str, icon='actions/player_play', title="MPV Playback"):
        subprocess.run([Stream.notify_cmd, '-r', '10010', '-i', icon, title, msg])

    def check_live(self):
        subprocess.check_output

    def run(self):
        subprocess.Popen(
            [Stream.player, self.url, *self.options])
        self.notify(self.rname)
        with open('/home/patrick/.config/mpv/nowplaying', 'w') as f:
            f.write(self.rname)

    @staticmethod
    def kill():
        subprocess.run(['pkill', Stream.player])
        with open('/home/patrick/.config/mpv/nowplaying', 'r+') as f:
            Stream.notify(
                f.readline(),
                'actions/player_stop')
            f.write('')

    def __init__(self, name: str, url: str):
        self.name = f"{len(streamlist)}: " + name
        self.rname = name
        self.url = url
        streamlist.append(self)


class YTStream(Stream):
    options = ['--no-video', '--ytdl-format=best[height<720]']


class TWStream(Stream):
    options = ['--ytdl-format=audio_only']


# Create and append all Streams

YTStream(
    "Future House Radio",
    "https://www.youtube.com/watch?v=YR0ZjnpHKFg")

TWStream(
    "Monstercat Radio",
    "https://twitch.tv/monstercat")

YTStream(
    "Random Chiptune Radio",
    "https://www.youtube.com/channel/UCf69z7VtcSTygbNKdFn4ELg/live")

YTStream(
    "Epic Music Radio",
    "https://www.youtube.com/channel/UC3zwjSYv4k5HKGXCHMpjVRg/live")

YTStream(
    "The Good Life Radio",
    "https://www.youtube.com/channel/UChs0pSaEoNLV4mevBFGaoKA/live")

YTStream(
    "Electro Swing Radio",
    "https://www.youtube.com/channel/UCl-Rh0PxCl0NblEbXIjeK3w/live")

# rofi part
r = rofi.Rofi()
i, key = r.select('Stream', [o.name for o in streamlist] + ['', '-> kill'])

# only on pressing return
if key == 0:
    if i == len(streamlist)+1:
        Stream.kill()
    else:
        streamlist[i].run()
