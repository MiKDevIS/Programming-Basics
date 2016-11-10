#include <stdio.h>

int main(){
        int a;
        printf("Please enter your number: ");
        scanf ("%d", &a);
        if (a>=0) {
                printf("Positive\n");
        } else {
                printf("Negative\n");
        }
        return 0;
}
