#include "tp3.h"

int     put_error(PrdCrt data)
{
    if (data.error_val == 1)
        fprintf(stderr, "Bad usage :\n./tp3 File1 File2\n");
    if (data.error_val == 2)
        fprintf(stderr, "Error allocation.\n");
    if (data.error_val == 3)
        fprintf(stderr, "Error file %s doesn't exist.\n", data.f1_nm);
    if (data.error_val == 4)
        fprintf(stderr, "Error file %s doesn't exist.\n", data.f2_nm);
    return (1);
}
