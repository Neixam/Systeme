NAME    =   tp3

SRC     =   src/

CNT     =   $(SRC)main.c                \
            $(SRC)parsing.c             \
            $(SRC)Produit_Cartesien.c   \
            $(SRC)put_error.c           \
            $(SRC)get_next_line.c       \
            $(SRC)data_s.c              \
            $(SRC)ft_base.c             \

OBJ     =   $(CNT:.c=.o)

FLAGS   =   -Wall       \
            -Werror     \
            -ansi       \
            -pedantic   \

HEADER  =   includes/

all     :   $(NAME)

$(NAME) :   $(OBJ)
	gcc $(FLAGS) $^ -o $(NAME) -I $(HEADER)

%.o     :   %.c
	gcc $(FLAGS) -o $@ -c $^ -I $(HEADER)

clean   :
	/bin/rm -rf $(OBJ)

bclean  :
	/bin/rm -rf $(NAME)

fclean  :   clean bclean

re      :   fclean all
