#include <stdio.h>
#include <stdlib.h>

int main()
{
    char str[]="the quick brown fox";
    char ch = 'b';
    char *pGot_char = NULL;
    pGot_char = strchr(str,ch);
    printf("%i this the address where it is stored",*pGot_char);
    return 0;
}
