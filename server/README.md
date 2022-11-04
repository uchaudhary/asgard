# Setting Up The Head Node

## Table of Contents

- [Setting Up The Head Node](#setting-up-the-head-node)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Requirements](#requirements)
    - [Operating System](#operating-system)
    - [Network Interfaces](#network-interfaces)
  - [Installation Steps](#installation-steps)

## About

This folder contains the scripts to setup the head node

## Requirements

### Operating System

These scripts have been tested to run on Ubuntu Server Edition 22.0.4 LTS.

### Network Interfaces

You will need two network interfaces for this to work.
Ideally, two ethernet ports.

## Installation Steps

> Please review the scripts prior to running them so that you know what to do

1. Run [`setupAvahi.bash`](setupAvahi.bash)
2. Run [`setupDNSMasq.bash`](setupDNSMasq.bash)
3. Run [`setupNFS.bash`](setupNFS.bash)
4. Copy all of the configs in [exampleConfigs](exampleConfigs) to either `/etc/` or to where the config file says to copy it
   1. Many of these scripts will need to be edited to work for your setup
