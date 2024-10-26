"""Fonction pour le TP de la séance 3 de génie logiciel.

Ce module ne contient qu'une fonction qui fait une prédiction sur la météo du jour
Dr Hugo Boisaubert - hugo.boisaubert@univ-nantes.fr

Exemple d'usage :
    meteo(prenom)
"""

def meteo(prenom:str) -> None:
    """Fonction qui affiche une prédiction météo à l'utilisateur.

    Pour faire sa prédiction cette fonction determine le nombre de lettre dans le
    prénom de l'utilisateur et s'il est pair affiche "Je pense qu'il va faire beau
    aujourd'hui" sinon "Je pense qu'il va pleuvoir aujourd'hui".

    Args:
      prenom:
        Une chaine de caractère représentant un prénom

    Returns:
      Rien

    """
    # Condition if qui utilise la fonction len() sur la variable prenom pour en déterminer le nombre de caractère
    # On y applique ensuite un modulo deux %2 afin de déterminer si il y a un reste dans une division euclidienne par 2
    if(len(prenom)%2 == 0):
        # Si le reste est bien égal à 0, alors le nombre de caractère est pair
        print("\n\nJe pense qu'il va faire beau aujourd'hui", prenom)
    else:
        # Si le reste n'est pas égal à 0, alors le nombre de caractère est impair
        print("\n\nJe pense qu'il va pleuvoir aujourd'hui", prenom)