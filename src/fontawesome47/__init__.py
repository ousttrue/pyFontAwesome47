import pathlib
import pkgutil
HERE = pathlib.Path(__file__).absolute().parent
DATA = 'fonts/fontawesome-webfont.ttf'


def get_path() -> pathlib.Path:
    return HERE / DATA


def get_data() -> bytes:
    return pkgutil.get_data('fontawesome47', DATA)
