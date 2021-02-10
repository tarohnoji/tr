#include <stdio.h>

int main(){
	int sato;
	sato = 100;
	fprintf(stderr, "sato=%d\n", sato);

	int *p;
	p = &sato;
	fprintf(stderr, "*p=%d\n", *p);
	return 0;
}
