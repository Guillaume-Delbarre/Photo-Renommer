from pathlib import Path

def renommer(file_path: Path, new_name: str) -> int :
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
    """
    # Vérification de la présence du fichier source
    if not file_path.exists() :
        return 2

    file_path.rename(file_path.parent / new_name)
    return 0


def get_all_files(dir_path: Path) -> list[Path]:
    """Récupère tous les fichiers d'un répertoire

    Parameters
    ----------
    dir_path : Path
        Chemin du répertoire des fichiers au format Path de pathlib

    Returns
    ----------
    list[Path] :
        Liste avec les fichiers au format Path de pathlib
    """
    if not dir_path.exists() or not dir_path.is_dir() :
        return []
    return [f for f in dir_path.iterdir()]


def order_files(files: list[Path], order: str = "Modifie", reverse: bool = False) -> list[Path] :
    """Tri la liste de fichier en fonction de la clé

    Parameters
    ----------
    files : list[Path]
        Liste des fichiers à trier
    
    order : str (defaut : "Modifie")
        Clé de trie de la liste
        valeurs possibles : "Modifie", "Cree", "Nom"

    reverse : bool (defaut : False)
        Trie croissant ou décroissant
        
    Returns
    ----------
    list[Path] :
        Retourne la liste triée
    """
    match order :
        case "Modifie" :
            return sorted(files, key=lambda path: path.stat().st_mtime, reverse=reverse)
        case "Cree" :
            return sorted(files, key=lambda path: path.stat().st_birthtime, reverse=reverse)
        case "Nom" :
            return sorted(files, key=lambda path: path.name, reverse=reverse)
        case _ :
            return files