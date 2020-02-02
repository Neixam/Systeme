#include "tp3.h"

int     parsing_enter(int ac, char **av, PrdCrt *data)
{
    if (ac != 3)
        return (1);
    if (!(data->f1_nm = ft_strdup(av[1])))
        return (2);
    if (!(data->f2_nm = ft_strdup(av[2])))
        return (2);
    if (!(data->f1 = fopen(data->f1_nm, "r")))
        return (3);
    if (!(data->f2 = fopen(data->f2_nm, "r")))
        return (4);
    return (0);
}
