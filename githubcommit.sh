#!/bin/bash

#cd linuxopg
sudo git add *
sudo git config --global user.email "markstendorf@hotmail.com"
sudo git config --global user.name "markstendorf"
echo Navn til commiten?
read commit
sudo git commit -m $commit
sudo git push
