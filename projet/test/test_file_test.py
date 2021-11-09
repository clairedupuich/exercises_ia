# **`Exercice`**:
# - créer un test pour définir une fonction my_sort qui fonctionne comme la méthode de liste sort(), elle est capable de trier dans l'ordre croissant une liste de nombres (int ou float), de string et de Booléen. Elle doit par contre renvoyer une erreur si on tente de trier une liste qui mélange les types
# - constuire ensuite cette fonction dans un autre fichier afin que ces tests passent avec succès.
# - consigne : pour le test vous avez le droit d'utiliser la methode sort mais pour votre fonction

import pytest

from file_test import my_sort


a = [2,3,1]
def test_my_sort():
    assert my_sort(a) == a.sort()
    assert type( ) == int or float or bool or str or list()


    


     
    
