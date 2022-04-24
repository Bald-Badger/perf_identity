all:
	gcc ./test.c -o wtf.elf

clean:
	sudo rm -f ./*.elf ./*.log ./*.old ./*.data ./*.csv