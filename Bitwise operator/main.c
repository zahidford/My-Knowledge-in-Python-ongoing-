/* This program show how to use different bitwise operators
    Created by Zahidul Amin
    Copy Right: 2019; */

#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned int a =60; // 0011 1100
    unsigned int b = 13; // 0000 1101
    int result = 0;
    int result2 = 0;
    int result3 = 0;
    int result4 = 0;
    result = a & b;
    result2 = a | b;
    result3 = a ^ b;
    result4 = a>>3;
//    0000 1100
    printf("Hello world!\n, %d %d %d %d", result,result2,result3,result4);
    return 0;
}
