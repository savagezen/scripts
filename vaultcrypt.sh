#!/usr/bin/sh

USER=/home/austin

cp -r $HOME/.ethereum $HOME/documents/vault/

tar -czf /tmp/vault.tar.gz $USER/documents/vault
tar -czf /tmp/keys.tar.gz $USER/documents/keys

gpg -e -r "Austin Haedicke" /tmp/vault.tar.gz
gpg -e -r "Austin Haedicke" /tmp/keys.tar.gz

mv /tmp/{vault,keys}.tar.gz.gpg $USER/documents/

rm /tmp/{vault,keys}.tar.gz
