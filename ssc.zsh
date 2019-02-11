#! /usr/bin/zsh

# scriptselect
ssc() {
    if [[ $# = 0 ]]
    then 
        cd $HOME/github/scripts/
    else
        file=$1;
        shift;
        $HOME/github/scripts/$file.* $*;
    fi
}
autoload ssc