import os

def renommer(file_path: str, new_name: str) -> int :
    """Renomme le fichier avec le nom donné

    Parameters
    ----------
    file_path : str
        Chemin du fichier à renommer
    new_name : str
        Nouveau nom du fichier (sans le path)

    Returns
    ----------
    int : 
        0 -> Le renommage s'est bien déroulé
        2 -> Erreur : Le fichier source n'est pas trouvé
        3 -> Erreur : Le programme n'a pas les privilèges pour renommer le fichier
    """

    # Vérification de la présence du fichier source
    if not os.path.isfile(file_path) :
        return 2
    
    # Récupération du chemin du répertoire du fichier
    dir_path = os.path.dirname(file_path)

    try :
        os.rename(file_path, dir_path + "/" + new_name)
    except FileNotFoundError :
        return 2
    except PermissionError :
        return 3
    
    return 0