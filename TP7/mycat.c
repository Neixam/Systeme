#include <stdio.h>

int     main(void)
{
    char    touche;

    while ((touche = getchar()) != EOF)
        putchar(touche);
    return (0);
}
