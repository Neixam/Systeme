#include "tp3.h"

int     ft_strlen(char *s)
{
    int     len;

    if (!s)
        return (0);
    for (len = 0; s[len]; len++);
    return (len);
}

char    *ft_strdup(char *s)
{
    char    *ret;
    int     len;
    int     i;

    len = ft_strlen(s);
    if (!(ret = (char*)malloc(sizeof(char) * (len + 1))))
        return (NULL);
    for (i = 0; i < len; i++)
        ret[i] = s[i];
    ret[i] = '\0';
    return (ret);
}
