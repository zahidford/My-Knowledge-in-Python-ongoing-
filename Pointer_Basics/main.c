#include <stdio.h>
#include <stdlib.h>

int main()
{
    int number1=25;
    int *pointer1=NULL;
    //int *address=NULL;
    pointer1= &number1;
    //*address= pointer;
    printf("Hello world The address of Pointer is %p\n",&pointer1);
    printf("Hello world The address of int Number is %p\n",&number1);
     printf("Hello world The address of pointer is pointing to %p\n",pointer1);
      printf("Hello world The value of Number is %d",number1);


    return 0;
}
