#! /bin/bash

TERM='/usr/local/bin/st'
EDITOR='/usr/bin/nvim'
PDFVIEW='/usr/bin/evince'

options="home\n- raspi2\n- raspi3\n\nUni\n- hel\n- hbpc9\n- m03"

option=$(echo -e ${options} | rofi -dmenu -p 'ssh')

case $option in
    "- raspi"* | "- m03" | "- hel" | "- hbpc"*)
        $TERM -e ssh ${option:2}
        ;;
esac

