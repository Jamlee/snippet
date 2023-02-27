#!/bin/bash
git submodule foreach bash push.sh
git add .
git commit -m 'feat(:memo:): update doc'
git pull
git push