#!/bin/bash

# Install chronyd
# Instructions from https://chrony.tuxfamily.org/doc/4.3/installation.html
# This installation requires that Homebrew is installed
# Run `./setupHomebrew.bash && source ~/.profile` prior to executing this script

brew install gcc pkg-config asciidoctor bison

brew link gcc

git clone https://git.tuxfamily.org/chrony/chrony.git chrony
cd chrony

# Installed to /usr/local
./configure

make
make docs

sudo make install
sudo make install-docs
