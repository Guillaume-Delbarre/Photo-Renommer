from src.renommer.renommer import renommer
from test.lib.file_manipulation import clear, jdd_path
from test.lib.file_check import file_exist, same_files

class TestRenommage :

    rep_value = "test_renommage"
    path_computed = jdd_path / "computed" / rep_value
    path_out = jdd_path / "out" / rep_value

    def clear(self)  -> None:
        clear(self.rep_value)

    def test_simplerenommage(self) -> None:
        self.clear()
        renommer(self.path_computed / "tt.txt", "new.png")
        assert file_exist(self.path_computed / "new.png")

    def test_contenurenommage(self)  -> None:
        self.clear()
        renommer(self.path_computed / "contenu", "renamed_contenu.txt")
        assert file_exist(self.path_computed / "renamed_contenu.txt")
        assert same_files(self.path_computed / "renamed_contenu.txt", self.path_out / "renamed_contenu.txt")