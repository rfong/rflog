#!/bin/zsh
if [ ! -z "$1" ]; then
  # use title as part of file name
  fname=_microblog/`date +"%Y-%m-%d"`-$1.md
else
  # no title
  fname=_microblog/`date +"%Y-%m-%d"`.md
fi

if [ -f "$fname" ]; then
  echo "$fname already exists."
else
  cp _microblog/_template.md $fname
  echo 'date: '`date +"%Y-%m-%d %H:%M:%S"` >> $fname
  echo "---" >> $fname
  echo "created $fname"
fi

# Open file for editing
vim $fname
