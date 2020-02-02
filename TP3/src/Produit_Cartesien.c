#include "tp3.h"

int     file_crt(PrdCrt data)
{
    char    *line1;
    char    *line2;
    int     ret1;
    int     ret2;

    for (ret1 = get_next_line(data.f1, &line1); ret1 != 0;
        ret1 = get_next_line(data.f1, &line1))
    {
        if (ret1 == 2)
            return (2);
        for (ret2 = get_next_line(data.f2, &line2); ret2 != 0;
            ret2 = get_next_line(data.f2, &line2))
        {
            if (ret2 == 2)
                return (2);
            printf("1%s%s\n", line1, line2);
            free(line2);
        }
        free(line1);
        rewind(data.f2);
    }
    return (0);
}
