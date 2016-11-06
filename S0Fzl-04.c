#include <stdio.h>

int main(){
    int a;
    printf("Please enter your number??\t");
    scanf ("%d", &a);
    if (a%2==0){
        printf("Even.\n");
    } else{
        printf("Odd.\n");
    }
    return 0;
}
