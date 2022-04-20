all:
	gcc ./test.c -o wtf.elf

clean:
	rm -f *.elf *.log *.old *.data