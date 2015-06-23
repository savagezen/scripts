#!usr/bin/zsh
# Reference - https://bbs.archlinux.org/viewtopic.php?id=136971

unixness () {
	T=$(sudo find {,/usr}/{{s,}bin,lib} /usr/include /boot /etc -type f ! -empty -printf "%s\n" | awk '{t+=$1} END {print t}')

	sudo find {,/usr}/{{s,}bin,lib} /usr/include /boot /etc -type f ! -empty -printf "%s\n" | awk -v t=$T '{p=$1/t; h += -p*log(p)/log(2)} END {print h}'
}

unixness
