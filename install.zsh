#! /usr/bin/zsh

echo -e "\\e[1;32m=> NOW PLACING SSC MODULE in '~/.zshrc.d/'\\e[0m"
mkdir -p $HOME/.zshrc.d && ln -sfvi $PWD/ssc.zsh $HOME/.zshrc.d

echo -e "\ndone."