all:	setup p1

setup:
	echo 0 > /proc/sys/kernel/randomize_va_space
	rm /bin/sh
	ln -s /bin/zsh /bin/sh

p1:
	gcc -g -fno-stack-protector -z execstack -mpreferred-stack-boundary=2 -o vuln1 vuln1.c
	sudo chown root vuln1
	sudo chgrp root vuln1
	sudo chmod +s vuln1
	python exploit1.py

p2:
	gcc -g -fno-stack-protector -mpreferred-stack-boundary=2 -o vuln2 vuln2.c
	sudo chown root vuln2
	sudo chgrp root vuln2
	sudo chmod +s vuln2
	python exploit2.py

p3:
	echo could not finish part3
