#!/usr/bin/env bash

MPVPIPE=/tmp/mpv_pipe
MPVFLAGS=--ytdl --ytdl-format='best[height<1100]'

if [ -z "$(pidof mpv)" ]; then

    mkfifo ${MPVPIPE} || echo ''
    echo "YT" > $HOME/.config/mpv/nowplaying
    /usr/bin/mpv ${MPVFLAGS} --input-file="${MPVPIPE}" "$(xclip -selection c -o)" & disown

    while [ -z "$(pidof mpv)" ]; do
        sleep 1
    done

else
    echo "loadfile \"$(xclip -selection c -o)\" append-play" >> "${MPVPIPE}"
fi

