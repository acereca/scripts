#! /bin/bash

options="Private\nPublic\nGit\nStud"

MUTT='neomutt'
option=$(echo -e ${options} | rofi -dmenu -p 'Mail')

MUTT_PROFILE=""
case $option in
    Private) MUTT_PROFILE=~/.config/mutt/private.muttrc;;
    Public) MUTT_PROFILE=~/.config/mutt/public.muttrc;;
    Stud) MUTT_PROFILE=~/.config/mutt/stud.muttrc;;
    Git) MUTT_PROFILE=~/.config/mutt/git.muttrc;;
    KIP) MUTT_PROFILE=~/.config/mutt/kip.muttrc;;
esac

if [ $# -gt 0 ]
then
    MUTT_PROFILE=$MUTT_PROFILE $1 neomutt
else
    MUTT_PROFILE=$MUTT_PROFILE neomutt
fi
