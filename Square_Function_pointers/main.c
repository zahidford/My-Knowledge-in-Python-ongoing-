#include <stdio.h>
#include <stdlib.h>
int function(int *ptr);
int main()
{
    int num =9;

    function(&num);
    printf("Hello world!\n the square of 9 is %d",num);
    return 0;
}

int function(int *ptr){
*ptr=*ptr*(*ptr);


}
