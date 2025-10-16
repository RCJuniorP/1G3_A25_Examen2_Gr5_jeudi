def mot_plus_long(liste_mots):
    """
    Retourne le mot le plus long d'une liste.
    Ignore les éléments qui ne sont pas des chaînes de caractères.

    :param liste_mots: liste de mots
    :return: le mot le plus long ou None si la liste est invalide ou vide
    """
    max_mot = ""
    try:
        for mot in liste_mots:
            try:
                if len(mot) > len(max_mot):
                    max_mot = mot
            except TypeError:
                pass

    except TypeError:
        print(f"Erreur. Impossible de trouver le mot le plus long dans {liste_mots}")

    if max_mot != "":
        return max_mot
    else:
        return None

def pourcentage_mots_max(mots, taille):
    """
    Calcule le pourcentage de mots ayant une longueur supérieure à une valeur donnée.

    :param mots: liste de mots
    :param taille: longueur minimale à comparer
    :return: pourcentage (float) de mots dépassant la taille, ou None si impossible
    """
    # Si mots n'est pas de type list
    if not isinstance(mots, list):
        print(f"Impossible de calculer le pourcentage. '{mots}' n'est pas une liste.")
        return None

    total_valide = 0
    count_sup = 0
    for mot in mots:
        if not isinstance(mot, str): # On doit ignorer tous les éléments qui ne sont pas des strings.
            continue
        total_valide += 1 # Le nombre d'éléments valides doit être incrementé si la valeur est valide (elle n'a pas été ignorée).
        longueur = len(mot)
        if longueur > taille: # On cherche les mots qui on une longeur supérieure à la taille.
            count_sup += 1 # Le nombre de mots dépassant la taille doit être incrementé par 1 et non assigné à 1.
    if total_valide == 0: # Il faut vérifier qu'il y ait au moins un élément valide pour éviter les divisions par 0.
        print("Impossible de calculer le pourcentage. Aucun élément valide.")
        return None
    pourcentage = (count_sup / total_valide) * 100
    return round(pourcentage, 2)

if __name__ == "__main__":
    animaux = ["chat", "chien", "éléphant", "souris", "hippopotame", 42, None, "oiseau"]
    print("Mot le plus long :", mot_plus_long(animaux))
    pourcentage = pourcentage_mots_max(animaux, 5)

    if pourcentage is not None:
        print("Pourcentage de mots de longueur maximale :", pourcentage, "%")
