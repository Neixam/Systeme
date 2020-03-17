import subprocess

def create_test() :
    ret = [["0", "0"], ["1", "0"], ["0", "1"], ["1", "1"],
            ["12", "12"], ["12", "-43"], ["-1", "-52"]]
    return (ret)

def nom_prenom(s) :
    prenom = s.split('_')[0]
    nom = s.split('_')[1]
    return (prenom, nom)

def check_verif(lst) :
    i = 0
    count = 0
    test = ["La somme de 0 et 0 vaut 0\n", "La somme de 1 et 0 vaut 1\n",
            "La somme de 0 et 1 vaut 1\n", "La somme de 1 et 1 vaut 2\n",
            "La somme de 12 et 12 vaut 24\n", "La somme de 12 et -43 vaut -31\n",
            "La somme de -1 et -52 vaut -53\n"]
    while (i < len(test)) :
        if test[i] == lst[i] :
            count += 1
        i += 1
    return (count)

def compil_file(lst) :
    ret = {}
    all_test = create_test()
    for elem in lst :
        elem2 = elem.replace(".c", "")
        elem2 = elem2.replace("Rendus_eleves/eleves_bis/", "")
        gcc = subprocess.run(["gcc", "-ansi", "-Wall", elem, "-o", elem2],
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        grep = subprocess.run(["grep", "-e", "/\\*", elem, "-c"], stdout=subprocess.PIPE)
        retour_grep = int(grep.stdout.decode())
        retour_gcc = gcc.stdout.decode()
        nb_Warning = retour_gcc.count("warning")
        prenom, nom = nom_prenom(elem2)
        if gcc.returncode == 0 :
            verif = []
            for test in all_test :
                execut = []
                execut.append("./" + elem2)
                execut.extend(test)
                execution = subprocess.run(execut, stdout=subprocess.PIPE)
                verif.append(execution.stdout.decode())
            ret[elem2] = (prenom, nom, 1, nb_Warning, check_verif(verif), retour_grep)
            subprocess.run(["rm", "-rf", elem2])
        else :
            ret[elem2] = (prenom, nom, 0, nb_Warning, 0, retour_grep)
    return (ret)


ret = subprocess.run(["find", "Rendus_eleves/", "-type", "f"], stdout=subprocess.PIPE)
lst = ret.stdout.decode().split('\n')
lst = lst[:-1]
dico = compil_file(lst)
fichier = open("Correction.csv", "w")
for key in dico :
    fichier.write(str(dico[key]).replace(" ", "").replace("'", "").replace("(", "").replace(")", "") + '\n')
fichier.close()
