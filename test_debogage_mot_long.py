import pytest
from debogage_mot_long import mot_plus_long, pourcentage_mots_max  # Remplacer par le nom de ton fichier

# ============================
# Tests pour mot_plus_long
# ============================

@pytest.mark.parametrize("liste_mots, resultat_attendu", [
    ("bientôt", None), # Ce test échoue parce que vu qu'un string est itérable qui produit d'autres strings, ce string
    # va agir comme une liste de lettres. Il ne sera donc pas détecté par le bloc try/except alors qu'il devrait être rejeté.
    (["finale", "bonjour", "vendre"], "bonjour"),
    (["faim", (1,2,3,4,5)], "faim"), # Ce test échoue parce que la seule chose qui est vérifée à propos des éléments de la liste
    # est le fait qu'ils ont une grandeur. Si l'opération len(element) est valide sur l'élément, l'élément ne sera pas ignoré.
    ([], None),
    (["son", "donner", "berger"], "donner")
])
def test_mot_plus_long(liste_mots, resultat_attendu):
    resultat_obtenu = mot_plus_long(liste_mots)
    assert resultat_attendu == resultat_obtenu
# ============================
# Tests pour pourcentage_mots_max
# ============================
def test_pourcentage_mots_max_normal():
    mots = ["poney", "girafe", "hippopotame", "chaton"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 75.0

def test_pourcentage_mots_max_tous_superieur():
    """
    Lorsque tous les mots présents dépassent la taille,
    le pourcentage retourné est 100%.
    """
    # TODO: Complèter ce test unitaire.
    assert False

def test_pourcentage_mots_max_elements_invalides():
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100.0

def test_pourcentage_mots_max_liste_vide():
    mots = []
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat is None

def test_pourcentage_mots_max_tous_inferieur():
    """
    Lorsque tous les mots présents sont
    plus petits que la taille, le pourcentage
    retourné est 0.0%.
    """
    # TODO: Ajouter le cas de test correspondant à la description
    #       au plan de tests et complèter ce test unitaire.
    assert False

def test_pourcentage_mots_max_tous_inferieur():
    mots = 7
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat == None