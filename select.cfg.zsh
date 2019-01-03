#! /bin/bash
options="i3wm\nranger keys\nranger scope\nvim\nzsh\nlivestreamer\nalpine"

option=$(echo -e ${options} | rofi -dmenu -p "Edit Config")

case $option in
    i3wm) termite -e "vim ~/.config/i3/config";;
    'ranger keys') termite -e "vim ~/.config/ranger/rc.conf";;
    'ranger scope') termite -e "vim ~/.config/ranger/scope.sh";;
    vim) termite -e "vim ~/.vimrc";;
    zsh) termite -e "vim ~/.zshrc";;
    livestreamer) termite -e "vim ~/.livestreamerrc";;
    alpine) termite -e "vim ~/.pinerc"
esac
