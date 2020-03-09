#include <stdio.h>
#include <stdlib.h>

int     main(int ac, char **av)
{
    int     touche;
    int     compteur;
    int     lenght;

    if (ac != 2)
        return (1);
    lenght = atoi(av[1]);
    for (compteur = 0; (touche = getchar()) != EOF; compteur++)
    {
        if (compteur != 0 && compteur % lenght == 0)
            fprintf(stderr, "%s : J'ai vu un paquet de %d caractères\n", av[0], lenght);
        putchar(touche);
    }
    return (0);
}
