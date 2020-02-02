#ifndef TP3_H
# define TP3_H
# include <stdio.h>
# include <stdlib.h>
# define BUFF_SIZE 1024

typedef struct  produit_cartesien
{
    int     error_val;
    char    *f1_nm;
    char    *f2_nm;
    FILE    *f1;
    FILE    *f2;
}               PrdCrt;

char            *ft_strdup(char *s);
int             get_next_line(FILE *f, char **line);
int             ft_strlen(char *s);
int             file_crt(PrdCrt data);
int             parsing_enter(int ac, char **av, PrdCrt *data);
int             put_error(PrdCrt data);
void            init_data(PrdCrt *data);
void            free_data(PrdCrt *data);

#endif
