#1 /bin/bash

ssh $1 -p 2222 am broadcast --user 0 -a net.acereca.automate.s8.ipcam.$2 < /dev/null > /dev/null 2> /dev/null
