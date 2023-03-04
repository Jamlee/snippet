#!/bin/bash
git submodule update --recursive --init
cd project; git checkout master; cd -
cd note; git checkout main; cd -
