from pathlib import Path

def renommer(file_path: Path, new_name: str) :
    """Renomme le fichier avec le nom donné

    Parameters
    ----------
    file_path : Path
        Chemin du fichier à renommer au format Path de pathlib
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
    if not file_path.exists() :
        return 2
    
    file_path.rename(file_path.parent / new_name)
    
    return 0