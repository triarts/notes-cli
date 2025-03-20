#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Error: Python3 is not installed. Please install it first."
    exit 1
fi

# Check if ~/.bashrc references ~/.bash_aliases
if ! grep -q ".bash_aliases" ~/.bashrc; then
    echo "Warning: .bashrc does not source .bash_aliases."
    echo "You may need to manually add this line to ~/.bashrc:"
    echo "if [ -f ~/.bash_aliases ]; then . ~/.bash_aliases; fi"
    exit 1
fi

# Ensure ~/.bash_aliases exists
if [ ! -f ~/.bash_aliases ]; then
    touch ~/.bash_aliases
    echo "Created ~/.bash_aliases"
fi

# Get the real path of notes.py
if [ ! -f "notes.py" ]; then
    echo "Error: notes.py not found in the current directory."
    exit 1
fi
dirPath=$(realpath notes.py)

# Check if an alias for "notes" already exists and remove it
sed -i '/^alias notes=/d' ~/.bash_aliases

# Add the new alias
echo "alias notes='python3 $dirPath'" >> ~/.bash_aliases
echo "Alias 'notes' updated to run: python3 $dirPath"

# Reload ~/.bash_aliases to apply changes immediately
source ~/.bash_aliases
echo "Alias applied! You can now use 'notes' in your terminal."
