#!/bin/sh
# https://www.wiki.archlinux.org/index.php/rxvt-unicode#Configuration

TERM=rxvt-256color command man -Pcat rxvt | sed -n '/depth: b/,/^BA/p'|sed '$d'|sed '/^       [a-z]/s/^ */^/g'|sed -e :a -e 'N;s/\n/@@/g;ta;P;D'|sed 's,\^\([^@]\+\)@*[\t ]*\([^\^]\+\),! \2\n! rxvt*\1\n\n,g'|sed 's,@@\(  \+\),\n\1,g'|sed 's,@*$,,g'|sed '/^[^!]/d'|tr -d "'\`" >> ~/.Xresources

