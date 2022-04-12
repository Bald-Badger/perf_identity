all:
	gcc ./test.c -o wtf

clean:
	rm -f ./wtf *.log *.old *.data