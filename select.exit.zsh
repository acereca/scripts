a=$(echo -e "Yes\nAbort" | rofi -dmenu -p 'Exit?')
if [[ 'Yes' = "$a" ]]; then
    exit 0
fi

exit 1
