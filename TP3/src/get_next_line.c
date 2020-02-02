#include "tp3.h"

char    *ft_strjoin(char *s1, char *s2, int boo)
{
    int     len;
    char    *ret;
    int     i;
    int     j;

    if (*s2 == '\0')
        return (s1);
    len = ft_strlen(s1) + ft_strlen(s2);
    if (!(ret = (char*)malloc(sizeof(char) * (len + 1))))
        return (NULL);
    for (i = 0; s1[i]; i++)
        ret[i] = s1[i];
    for (j = 0; i + j < len; j++)
        ret[i + j] = s2[j];
    ret[i + j] = '\0';
    if (boo == 1 || boo == 3)
        free(s1);
    if (boo > 1)
        free(s2);
    return (ret);
}

int     get_line(char *buff, int size, FILE *f)
{
    int     chr;
    int     i;

    i = 0;
    for (chr = getc(f); chr != EOF && i < size - 1; chr = getc(f))
    {
        if (chr == '\n')
        {
            buff[i] = '\0';
            return (3);
        }
        buff[i] = chr;
        i++;
    }
    buff[i] = '\0';
    if (chr == EOF)
        return (0);
    return (1);
}

int     get_next_line(FILE *f, char **line)
{
    char    buff[BUFF_SIZE];
    int     ret;
    
    if (!(*line = (char*)malloc(sizeof(char))))
        return (2);
    **line = '\0';
    do{
        ret = get_line(buff, BUFF_SIZE, f);
        if (!(*line = ft_strjoin(*line, buff, 1)))
            return (2);
    }while (ret == 1);
    return (ret);
}
