#!/bin/bash
DATE=`date +%d-%m-%Y`
# git pull
git add -A
git commit -m $DATE
git push -u origin main