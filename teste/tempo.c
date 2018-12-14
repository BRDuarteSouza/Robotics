#include<time.h>
#include<stdio.h>

int main(void){
time_t  now;
long ls_report;
//time(&now);

ls_report = now;
while(1){
	time(&now);

	printf("Agora: %ld \n", now);
	//printf("testando .... %ld \n", casa);
	if(now-ls_report >= 5){
		printf("Saindo");
		break;
		}
	}
return 0;

}
