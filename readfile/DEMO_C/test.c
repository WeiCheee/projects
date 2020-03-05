#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    char ch;
    while(ch!='\r'){
        ch = getchar();
        // printf("sss123");
        putchar(ch);
    }
    
    // printf("sdsd\n");
    system("pause");
    return 0;
}
