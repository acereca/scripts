#! /bin/bash

options="Private\nPublic\nGit\nStud\nKIP"

TERM='/usr/bin/kitty'
MUTT='neomutt'
option=$(echo -e ${options} | rofi -dmenu -p 'Mail')

case $option in
    Private) MUTT_PROFILE=~/.config/mutt/private.muttrc ${TERM} -e ${MUTT} &;;
    Public) MUTT_PROFILE=~/.config/mutt/public.muttrc ${TERM} -e ${MUTT} &;;
    Stud) MUTT_PROFILE=~/.config/mutt/stud.muttrc ${TERM} -e ${MUTT} &;;
    Git) MUTT_PROFILE=~/.config/mutt/git.muttrc ${TERM} -e ${MUTT} &;;
    KIP) MUTT_PROFILE=~/.config/mutt/kip.muttrc ${TERM} -e ${MUTT} &;;
esac
