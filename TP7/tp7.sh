# Question 3 :
gcc -o first mycat2.c && gcc -o second mycat2.c
man ls | ./first 1500 | ./second 1500 > /dev/null
# On voit que les exécutions s'entremêlent et que donc il ne peut pas être en série
