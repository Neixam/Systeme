#include "tp3.h"

void    init_data(PrdCrt *data)
{
    data->error_val = 0;
    data->f1 = NULL;
    data->f2 = NULL;
    data->f1_nm = NULL;
    data->f2_nm = NULL;
}

void    free_data(PrdCrt *data)
{
    if (data->f1)
        fclose(data->f1);
    if (data->f2)
        fclose(data->f2);
    if (data->f1_nm)
        free(data->f1_nm);
    if (data->f2_nm)
        free(data->f2_nm);
}
