#!/bin/sh

# Usage:
# tabc.sh <tabbed-id> <command>
# Commands:
#    add <window-id> 	- Add window to tabbed
#    remove <window-id> - Remove window from tabbed
#    list				- List all clients of tabbed

#
# Functions
#

# Get wid of root window
function get_root_wid {
	xwininfo -root | awk '/Window id:/{print $4}'
}

# Get children of tabbed
function get_clients {
	id=$1
	xwininfo -id $id -children | sed -n '/[0-9]\+ \(child\|children\):/,$s/ \+\(0x[0-9a-z]\+\).*/\1/p'
}

# Get class of a wid
function get_class {
	id=$1
	xprop -id $id | sed -n '/WM_CLASS/s/.*, "\(.*\)"/\1/p'
}

#
# Main Program
#

#tabbed=$1; shift
tabbed=$(xwininfo -root -tree | grep '"tabbed" "tabbed"' | awk '{print $1}')
if [ "$(get_class $tabbed)" != "tabbed" ]; then
	echo "Not an instance of tabbed" 2>&1;
    exit
fi

cmd=$1

case $cmd in
	add)
        dunstify "Tabbed" "adding instnce to ${tabbed}"
        wid=$(xwininfo | grep "id:" | cut -d" " -f4)
		xdotool windowreparent $wid $tabbed
		;;
	remove)
        dunstify "Tabbed" "removing instance from ${tabbed}"
        wid=$(xwininfo | grep "id:" | cut -d" " -f4)
		xdotool windowreparent $wid $(get_root_wid)
		;;
	list)
		get_clients $tabbed
		;;
esac
