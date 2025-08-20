from test.lib.file_manipulation import clear, jdd_path
from src.renommer.renommer import get_all_files, order_files


class TestGetFiles :

    rep_value = "test_get_files"
    path_computed = jdd_path / "computed" / rep_value
    path_out = jdd_path / "out" / rep_value

    def clear(self)  -> None:
        clear(self.rep_value)


    def test_getfiles(self) -> None :
        self.clear()
        files = get_all_files(self.path_computed)
        ordered_files = [f.name for f in order_files(files, order="Nom")]
        assert ordered_files == ['file_1.txt', 'file_3.txt', 'file_4.txt', 'zfile_2.txt']

