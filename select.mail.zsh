#! /bin/bash

options="Private\nPublic\nGit\nStud\nKIP"

TERM='/usr/local/bin/st'
option=$(echo -e ${options} | rofi -dmenu -p 'Mail')

case $option in
    Private) MUTTPROFILE=~/.mutt/muttrc.private.private ${TERM} -e mutt &;;
    Public) MUTTPROFILE=~/.mutt/muttrc.public.private ${TERM} -e mutt &;;
    Stud) MUTTPROFILE=~/.mutt/muttrc.stud.private ${TERM} -e mutt &;;
    Git) MUTTPROFILE=~/.mutt/muttrc.git.private ${TERM} -e mutt &;;
    KIP) MUTTPROFILE=~/.mutt/muttrc.kip.private ${TERM} -e mutt &;;
esac
