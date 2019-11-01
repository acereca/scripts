#! /usr/bin/zsh

#mountpoint /mnt/psrv || sshfs bahamut:/ /mnt/psrv

cd ~/gitlab/keys/
git pull

$HOME/.local/bin/keepmenu; git diff-index --quiet HEAD || git add Passwords.kdbx && git commit -m "$(date)" && git push
