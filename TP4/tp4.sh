#!/bin/bash

# Exercice 1

# Question 1
head -5 /etc/passwd

# Question 2
cat /bin/chmod

# Question 3
strings /bin/chmod | grep "\.so"

# Question 4
ls -la ~

# Question 5
man man | grep -e "^$" | wc -l

# Question 6
ls -l /bin/ | cut -d " " -f 1  | grep "x$" | wc -l

# Question 7
grep -e "#include <stdlib.h>" ~ -R | wc -l


# Exercice 2

# Question 1
sort fichier1.csv > fichier11.csv
sort fichier2.csv > fichier22.csv
# Lignes uniquement dans fichier1 1000
comm -3 -2 fichier11.csv fichier22.csv | wc -l
# Lignes uniquement dans fichier2 921
comm -3 -1 fichier11.csv fichier22.csv | wc -l
# Lignes qui sont dans les deux fichiers 241
comm -1 -2 fichier11.csv fichier22.csv | wc -l

# Question 2
comm -3 fichier11.csv fichier22.csv > fichier3.csv

# Question 3
cut fichier3.csv -d "," -f 2,3 | sort | uniq -d

# Question 4
cut fichier3.csv -d "," -f 2,3,4 | sort | uniq -d

# Question 5
cut fichier3.csv -d "," -f 4 | sort -n | uniq -c

# Question 6
cut fichier3.csv -d "," -f 4 | sort -n | uniq -c | sort -rn | head -5

# Question 7
cut fichier3.csv -d "," -f 2 | sort | uniq -c | sort -n | tail -1

# Question 8
# On peut effectivement considérer ce premier champs comme un clé premaire car lorsque l'on lance la commande ci-dessous :  
cut fichier3.csv -d "," -f 1 | sort | uniq -c
# on remarque que toutes les occurences de chaque champs sont uniques car leur décompte est de 1.

# Exercice 3

# Question 1
ls -lR ~ | grep "^d" | wc -l

# Question 2
ls -lR ~ | grep "^-" | wc -l

# Question 3
grep -e "#include" -R ~ -C 750 -h | wc -l

# Question 4
grep -e "#" -R ~ | grep "\.py:" | cut -d "#" -f 2 | wc -c

# Question 5
man find | grep -i "[^a-zA-Z]le[^a-zA-Z]" | sed -e s/'[^a-zA-Z][Ll]e[^a-zA-Z]'/'\nle '/g | cut -d " " -f 1 | grep -xv "" | wc -l

# Question 6
grep -vhe '#' -e '/\*' -e '\*/' -e '//' -e '*' -e '^$' -e 'extern' -e 'typedef' -R /usr/include/ | grep -e ');$' | wc -l

# Question 7
ps -e | tail -c +29 | wc -l

# Question 8
ls -l /proc/ | grep -e '^d' | grep -e '[0-9]$' | wc -l

# Question 9
ls -l /proc/ | grep -e '^d' | grep -e '[0-9]$' | cut -d " " -f 4 | sort | uniq -c | sort -n | tail -1
