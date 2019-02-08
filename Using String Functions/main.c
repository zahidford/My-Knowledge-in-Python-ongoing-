#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char my_string[]="This is a string duh!!";
    char temp[100];

    strncpy(temp,my_string,sizeof(temp)-1);
    //using length

    printf("Hello world!\n  The length of the string is %d \n ", strlen(my_string));
    printf("Hello world!\n  The  string temp says %s ", temp);

    // concatnation
    strncat(temp,my_string,10);
    printf("Hello world!\n  The  string temp says after concatnation %s ", temp);
    // compare

    printf("The letter \"A\" and letter \"A\" is %d\n",strcmp("A","A"));
    printf("The letter \"love\" and letter \"evol\" is %d\n",strcmp("love","evol"));
    return 0;
}
