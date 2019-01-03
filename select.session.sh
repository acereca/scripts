#! /bin/bash

TERM='/usr/local/bin/st'
EDITOR='/usr/bin/nvim'
PDFVIEW='/usr/bin/evince'

options="D&D Homebrew\nVision(s)"

option=$(echo -e ${options} | rofi -dmenu -p "Select Session")

case $option in
    'D&D Homebrew')
        i3-msg "append_layout ~/.config/i3/dnd_vim.json"
        ${PDFVIEW} ~/gitlab/dnd/homebrew.pdf &
        ${TERM} -e ${EDITOR} -c 'lcd ~/gitlab/InternReport' +NERDTree &
        ;;
    'Vision(s)')
        #i3-msg "append_layout ~/.config/i3/dnd_vim.json"
	ssh -fNL 8888:localhost:8888 m10 || echo 'already bound to :8888'
	~/gitlab/BaTh/data/sshfs.sh
        code ~/gitlab/BaTh/data/remote_proj/pit.code-workspace
        ;;
esac

