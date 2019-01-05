#! /usr/bin/zsh

# scriptselect
ssc() {
    if [[ $# = 0 ]]
    then 
        cd $HOME/github/scripts/
    else
        $HOME/github/scripts/$1.* $2;
    fi
}
autoload ssc