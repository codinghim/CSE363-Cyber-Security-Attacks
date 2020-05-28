# HW4 Buffer Overflow Exploitation

Author: Daniel Himchan Yun, Stony Brook University CSE363

1. I used the following command to find the shellcode that does not contain bytes between x68 and x6e. 

	msfvenom -p linux/x86/exec CMD=/bin/zsh -b '\x68\x69\x6a\x6b\x6c\x6d\x6e' -f python

2. I used the same method of ret2libc described in the lecture. I found the address where libc code resides and offsets of system and exit. I also neeeded system arguments(\bin\sh) which could be found using strings. Then, I constructed a buffer string with format of JUNK bytes(of 264 bytes until stack pointer where it affects eip) + address of libc system function + address of libc exit function + system argument(/bin/sh string). I called subprocess to run ./vuln2 with the buffer string as an argument.

3. Could not finish

** I could run it with command line commands python exploit1.py but it failed to run in make file. Please test it with pure command lines if makefile does not work.
