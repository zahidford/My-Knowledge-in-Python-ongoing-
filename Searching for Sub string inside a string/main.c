#include <stdio.h>
#include <stdlib.h>

int main()
{
    char str[]="the quick brown dog";
    char ch[] = "dog";
    char *pGot_char = NULL;
    pGot_char = strstr(str,ch);
    printf("%i this the address where it is stored",*pGot_char);
    return 0;
}
