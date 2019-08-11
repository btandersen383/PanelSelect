#!/bin/bash

# used to copy all files from the staging space to the sublime packages space
# I do this so small changes here don't immediately affect sublime

echo "copying over project files"

DEST=~/.config/sublime-text-3/Packages/PanelSelect

cp -r "keymaps" $DEST
cp -r "menus" $DEST
cp "PanelSelect.py" $DEST
cp "PanelSelect.sublime-commands" $DEST
