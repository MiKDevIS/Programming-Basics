#include <stdio.h>

int main(){
    float a;
    printf("Please enter your student point??\t");
    scanf ("%f", &a);
    if (a>=0 && a<=20){
        if (a>=10)
            printf("Pass.\n");
        else
            printf("Fail.\n");
    } else{
        printf("your student point is out of range.\n");
    }
    return 0;
}
