a=$(echo -e "Yes\nAbort" | rofi -dmenu -p 'Exit?')
echo $a
if [[ 'Yes' = "$a" ]]; then
    i3-msg exit;
fi
