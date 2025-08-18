from pathlib import Path
import shutil

ici = Path.cwd()
print(ici)

ressources = ici / "test/ressources"
print(ressources)

print(ressources.exists())
print(ressources.is_dir())

################################

out = ressources / "jdd/out/test_01"
if out.exists() and out.is_dir() :
    shutil.rmtree(out)

################################

print("\nressources/jdd : ")
for f in (ressources/"jdd/in/test_renommage").iterdir():
    print(f.name)
    print(f.stem)
    print(f.parent)
    # f.rename(f.parent)

################################

# shutil.copytree((ressources/"jdd/in/test_renommage"), (ressources / "jdd/out/test_renommage"))