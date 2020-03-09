#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int     main(int ac, char **av)
{
    int             touche;
    int             compteur;
    int             lenght;
    clockid_t       id_start;
    struct timespec temps_start;
    clockid_t       id_end;
    struct timespec temps_end;
    long int        char_avg;
    float        secondes;

    if (ac != 2)
        return (1);
    lenght = atoi(av[1]);
    clock_gettime(id_start, &temps_start);
    for (compteur = 0; (touche = getchar()) != EOF; compteur++)
    {
        if (compteur != 0 && compteur % lenght == 0)
            fprintf(stderr, "%s : J'ai vu un paquet de %d caractères\n", av[0], lenght);
        putchar(touche);
    }
    clock_gettime(id_end, &temps_end);
    secondes = (temps_end.tv_nsec * 1.0 - temps_start.tv_nsec * 1.0) / 1000000000;
    char_avg = compteur / secondes;
    fprintf(stderr, "%s : NB TOTAL CARACTÈRES : %d\n%s : TPS TOTAL EXÉCUTION : %f\n%s : VITESSE MOYENNE FINALE : %ld chars par seconde\n",
            av[0], compteur, av[0], secondes, av[0], char_avg);
    return (0);
}
