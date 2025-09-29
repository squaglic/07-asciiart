"""Encodage d'une chaîne de caractères."""
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    S = []  # résultat : liste de tuples (caractère, nombre)
    O = [1]  # liste des compteurs d'occurrences pour chaque bloc
    C = [s[0]]  # liste des caractères correspondant à chaque bloc
    k = 1
    n = len(s)
    # condition d'arrêt : tant que k < n on continue d'examiner la chaîne
    while k < n:
        # si le caractère courant prolonge le bloc précédent
        if s[k] == s[k-1]:
            O[-1] += 1  # incrémenter le compteur du bloc courant
        else :
            # nouveau bloc : ajouter le caractère et initialiser son compteur
            C += s[k]
            O += [1]
        k += 1
    # construction finale du résultat en zippant les deux listes
    for x in zip(C, O):
        S.append(x)
    return S


def artcode_r(s: str):
    """Renvoie la liste de tuples (caractère, nombre d'occurrences consécutives)
    de la chaîne s, de façon récursive (Run-Length Encoding)."""
    # cas de base : chaîne vide
    if not s:
        return []

    # compter la longueur de la première série
    k = 1
    while k < len(s) and s[k] == s[0]:
        k += 1

    # tête : (premier caractère, longueur de la série)
    # queue : encoder récursivement le reste
    return [(s[0], k)] + artcode_r(s[k:])

#### Fonction principale

def main():

    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
