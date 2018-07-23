#!/usr/bin/sh

# taken from:
# http://www.slideshare.net/Ovid/perl-6-for-mere-mortals

seven () {
  echo "-----------------"
  echo "X = 7 / 2        "
  echo "-----------------"
  echo -n "perl     | " ; perl -E 'say 7/2'
  echo -n "python 3 | " ; python -c 'print (7/2)'
  echo -n "python 2 | " ; /usr/bin/python2.7 -c 'print 7/2'
  echo -n "ruby     | " ; ruby -e 'puts 7/2'
  echo -n "shell    | " ; echo $((7/2))
  echo -n "bc       | " ; echo "7/2" | bc
}

neg_seven () {
  echo "-----------------"
  echo "X = -7 / 2       "
  echo "-----------------"
  echo -n "perl     | " ; perl -E 'say -7/2'
  echo -n "python 3 | " ; python -c 'print (-7/2)'
  echo -n "python 2 | " ; /usr/bin/python2.7 -c 'print -7/2'
  echo -n "ruby     | " ; ruby -e 'puts -7/2'
  echo -n "shell    | " ; echo $((-7/2))
  echo -n "bc       | " ; echo "-7/2" | bc
}

zero () {
  echo "-----------------"
  echo "X = .1 + .2 - .3 "
  echo "-----------------"
  echo -n "perl6    | " ; perl6 -e 'say .1 + .2 - .3'
  echo -n "perl     | " ; perl -E 'say .1 + .2 - .3'
  echo -n "python 3 | " ; python -c 'print (-7/2)'
  echo -n "python 2 | " ; /usr/bin/python2.7 -c 'print -7/2'
  echo -n "ruby     | " ; ruby -e 'puts -7/2'
  echo -n "shell    | " ; echo $((-7/2))
  echo -n "bc       | " ; echo "-7/2" | bc
}

divided_by_zero () {
  echo "-----------------"
  echo "1 / 0            "
  echo "-----------------"
  echo -n "perl6    | " ; perl6 -e 'say 1/(.1 + .2 - .3)'
  echo -n "perl     | " ; perl -E 'say 1/(.1 + .2 - .3)'
  echo -n "python 3 | " ; python -c 'print (1/(.1+.2-.3))'
  echo -n "python 2 | " ; /usr/bin/python2.7 -c 'print 1/(.1+.2-.3)'
  echo -n "ruby     | " ; ruby -e 'puts 1/(0.1+0.2-0.3)'
  echo -n "shell    | " ; echo "syntax error: invalid arithmetic operator"
  #			  echo $(1/(.1+.2-.3)))
  echo -n "bc       | " ; echo "1/(.1+.2-.3)" | bc
}

sun_mass () {
  echo "-----------------"
  echo "(mass of sun) * 0"
  echo "-----------------"
  echo -n "perl     | " ; perl -E 'say 1.99E30 * (.1 + .2 - .3)'
  echo -n "python 3 | " ; python -c 'print (1.99E30 * (.1+.2-.3))'
  echo -n "python 2 | " ; /usr/bin/python2.7 -c 'print 1.99E30*(0.1+0.2-0.3)'
  echo -n "ruby     | " ; ruby -e 'puts 1.99E30*(0.1+0.2-0.3)'
  echo -n "shell    | " ; echo "syntax error: invalid arithmetic operator"
  #			  echo $((1.99E30*(.1+.2-.3)))
  echo -n "bc       | " ; echo "1.99E30*(.1+.2-.3)" | bc
}

selection () {
  echo "Solve for X"
  PS3='Choose an equation (1-5): '
  options=("X = 7 / 2" 
    "X = -7 / 2" 
    "X = .1 + .2 - .3" 
    "X = 1 / 0" 
    "(mass of sun) * 0" 
    "Quit")
  select opt in "${options[@]}"
  do
    case $opt in
	"X = 7 / 2")
	  seven
	  ;;
	"X = -7 / 2")
	  neg_seven
	  ;;
	"X = .1 + .2 - .3")
	  zero
	  ;;
	"X = 1 / 0")
	  divided_by_zero
	  ;;
	"(mass of sun) * 0")
	  sun_mass
	  ;;
	"Quit")
	  break
	  ;;
	*) echo invalid option;;
    esac
  done
}

selection
