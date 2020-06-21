#!/bin/sh

bspc query -D --names | {
    while true; do
        IFS=$'\t' read -ra desks << "${bspc query}"
}

