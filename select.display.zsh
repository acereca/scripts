#!/bin/sh

choicearr=("        " "          " "  " "     = " "")
IFS=$'\n' eval 'choices="${choicearr[*]}"'

chosen=$(echo -e "${choices}" | rofi -dmenu -p "Screen Setup")

connected=($(xrandr | grep '\bconnected\b' | awk '{print $1}'))

case "$chosen" in
	${choicearr[0]}) xrandr --output "${connected[0]}" --auto --output "${connected[1]}" --off;;
        ${choicearr[1]}) xrandr --output ${connected[0]} --primary --auto --output ${connected[1]} --auto --right-of ${connected[0]};;
        ${choicearr[2]}) xrandr --output ${connected[1]} --auto --output ${connected[0]} --primary --auto --right-of ${connected[1]};;
        ${choicearr[3]}) xrandr --output "${connected[1]}" --auto --same-as ${connected[0]};;
	${choicearr[4]}) arandr ;;
esac

# redo for added keyboards
setxkbmap -option caps:escape

# Relaunch polybar if there was a selection.
[ "$chosen" == "" ] || i3-msg restart
