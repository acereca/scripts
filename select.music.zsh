#! /bin/bash

options="EpicMusic\nMA Lite\nMagicalMusic\nMonstercat\nSensualMusique\nRelaxBeats\n\n-> kill <-"

option=$(echo -e ${options} | rofi -dmenu -p 'Musik')

novideo="--no-video --ytdl-format 94 "

case $option in
    'Monstercat')
        mpv "ytdl://twitch.tv/monstercat" --ytdl-format="audio_only" & ;;
    SensualMusique)
        mpv 'https://www.youtube.com/sensualmusique1/live' $novideo & ;;
    RelaxBeats)
        mpv "ytdl://twitch.tv/relaxbeats" --ytdl-format="audio_only" & ;;
    MagicalMusic)
        mpv "https://www.youtube.com/user/MagicalMusicChannel/live" $novideo & ;;
    EpicMusic)
        mpv "https://www.youtube.com/user/epicmusicvn/live" $novideo & ;;
    '-> kill <-')
        pkill mpv
        option='';;
esac

echo $option > ~/.config/mpv/nowplaying
