#include "tp3.h"

int     main(int ac, char **av)
{
    PrdCrt  data;

    init_data(&data);
    if ((data.error_val = parsing_enter(ac, av, &data)))
    {
        free_data(&data);
        return (put_error(data));
    }
    if ((data.error_val = file_crt(data)))
    {
        free_data(&data);
        return (put_error(data));
    }
    free_data(&data);
    return (0);
}
