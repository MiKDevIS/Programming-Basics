#include <stdio.h>

int main(){
        int r;
        float surface,perimeter;
        printf("Please enter radius of circle: ");
        scanf("%d",&r );
        surface = 3.14 * r * r;
        perimeter = 2 * 3.14 * r;
        printf("Surface: %f \n",surface);
        printf("Perimeter: %f ",perimeter);
        return 0;
}
