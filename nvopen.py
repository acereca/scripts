#!/usr/bin/env python

import subprocess
import neovim
import sys, os

try:
    nv = neovim.attach('socket', path="/tmp/nvim-ln")
    nv.command(":e " + sys.argv[1])

except Exception as e:
    print(e)
    envir = os.environ.copy()
    envir['SOCK'] = '/tmp/nvim-ln'
    subprocess.call(
        ['nvim', sys.argv[1]],
        env=envir
    )
