""" Mon pti module
"""

def meteo(prenom:str) -> None:
    """Fonction qui affiche un truc et retourne rien ! 

    """
    # Condition if 
    if(len(prenom)%2 == 0):
        # Si  pair
        print("\n\nJe pense qu'il va faire beau aujourd'hui", prenom)
    else:
        # Si pas mpair
        print("\n\nJe pense qu'il va pleuvoir aujourd'hui", prenom)