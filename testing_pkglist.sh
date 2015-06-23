#!/bin/zsh

FILE=$HOME/.testing-pkgslist

echo "Testing Repo:" > $FILE
paclist testing >> $FILE

echo -e "\nCommunity-Testing Repo:" >> $FILE
paclist community-testing >> $FILE

echo -e "\nMultilib-Testing Repo:" >> $FILE
paclist multilib-testing >> $FILE
