#!/usr/bin/env bash

MPVPIPE=/tmp/mpv_pipe

if [ -z "$(pidof mpv)" ]; then

    /usr/bin/mpv --no-terminal --input-file="${MPVPIPE}" "${1}" & disown

    while [ -z "$(pidof mpv)" ]; do
        sleep 1
    done

else
    echo "loadfile \"${1}\" append-play" >> "${MPVPIPE}"
fi

