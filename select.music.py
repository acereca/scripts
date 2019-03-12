#! /usr/bin/env python3
import subprocess
import abc
import rofi
import sys, inspect

class Stream(object):
    player = 'mpv'
    notify_cmd = 'dunstify'

    @staticmethod
    def notify(msg: str, icon='player_play'):
        subprocess.run([Stream.notify_cmd, '-r', '10010', '-i', icon, msg])

    def run(self):
        subprocess.Popen([Stream.player, self.url, *self.options], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.notify(f'started live playback of:<br/>{self.name}')
        with open('/home/patrick/.config/mpv/nowplaying', 'w') as f:
            f.write(self.name)

    @staticmethod
    def kill():
        subprocess.run(['pkill', Stream.player])
        with open('/home/patrick/.config/mpv/nowplaying', 'r+') as f:
            Stream.notify(f'stopped live playback of:<br/>{f.readline()}', 'player_stop')
            f.write('')

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

class YTStream(Stream):
    options = ['--no-video', '--ytdl-format=94']

class TWStream(Stream):
    options = ['--ytdl-format=audio_only']


# Create and append all Streams

streamlist = [
    YTStream(
        "Best of Epic Music",
        "https://www.youtube.com/channel/UC3zwjSYv4k5HKGXCHMpjVRg/live"),

    TWStream(
        "Monstercat Radio",
        "https://twitch.tv/monstercat"),
    
    YTStream(
        "Electro Swing Radio", 
        "https://www.youtube.com/channel/UCl-Rh0PxCl0NblEbXIjeK3w/live"),
    
    YTStream(
        "The Good Life Radio",
        "https://www.youtube.com/channel/UCVeETS7uZTAARqvv2zssZCw/live")
]

        
# rofi part

r = rofi.Rofi()
i, key = r.select('Stream', [o.name for o in streamlist] + ['','-> kill'])

# only on pressing return
if key == 0:
    if i == len(streamlist)+1:
        Stream.kill()
    else: 
        streamlist[i].run()
