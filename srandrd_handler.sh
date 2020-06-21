#!/bin/sh

nocon=$(xrandr | grep " connected " | wc -l)
noact=$(xrandr --listactivemonitors | head -n1 | cut -d" " -f2)

noconold=$(cat $HOME/github/scripts/.dpcon)

act=$(xrandr --listactivemonitors | tail -n${noact} | awk -F"+" '{print $2}' | awk '{print $1}')

if [ $noact -ne $noactold ]; then
    dunstify "Monitor change (${noact}/${nocon})" "${noconold} -> ${nocon}";
fi

echo "${nocon}" > $HOME/github/scripts/.dpcon
