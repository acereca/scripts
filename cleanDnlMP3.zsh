#!/usr/bin/zsh

source /home/patrick/.zshrc
cd /home/patrick/Musik

zmv '(*): (*) - (*).mp3' '$2 - $3.mp3'
zmv '(*): (*).mp3' '$1 - $2.mp3'
zmv '(*) \[(*)\].mp3' '$1.mp3'
zmv '(*) \(Out Now\)(*)' '$1$2'

