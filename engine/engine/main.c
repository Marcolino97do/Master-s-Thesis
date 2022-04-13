//
//  main.c
//  engine
//
//  Created by Marco Eterno on 18/10/21.
//

#include <stdio.h>
#include <string.h>

int main()
{
    int i=77;
    char destination[32] = "Hello ";
    char source[32];
    source= sprinf(i);
    strcat(destination,source);
    printf("Concatenated String: %s\n", destination);
    return 0;
}
