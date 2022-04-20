#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
 
uint64_t Fibonacci(uint64_t n)
{
	if ( n == 0 )
		return 0;
	else if ( n == 1 )
		return 1;
	else
		return ( Fibonacci(n-1) + Fibonacci(n-2) );
} 


int main(int argc, char *argv[])
{
	uint64_t n = 0;
	int i = 0;
	int c;

	n = 42;
 
	printf("%lu\n", Fibonacci(n));

	return 0;
}
 
