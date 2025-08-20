from pathlib import Path
import shutil

jdd_path=Path.cwd() / "test/ressources/jdd"

def clear(name_dir: str)  -> None:
    clear_computed(name_dir)
    copy_from_input(name_dir)

def clear_computed(name_dir: str)  -> None:
    path = jdd_path / "computed" / name_dir

    if path.exists() and path.is_dir() :
        shutil.rmtree(path)

def copy_from_input(name_dir: str) -> None :
    path_computed = jdd_path / "computed" / name_dir
    path_input = jdd_path / "in" / name_dir

    if path_input.exists() and path_input.is_dir() :
        if not path_computed.exists() :
            shutil.copytree(path_input, path_computed)
        else :
            print(f"[ERREUR] : La cible : {path_computed} existe déjà, elle n'a pas été supprimée")
    else :
        print(f"[ERREUR] : Le répertoire source : {path_input} n'existe pas ou n'est pas un répertoire")