import pathlib

HERE = pathlib.Path(__file__).absolute().parent


def main(dst: pathlib.Path):
    import fontawesome47.icons

    with dst.open('w') as w:
        for item in fontawesome47.icons.get_icons():
            unicode = item['unicode']
            name = item["id"].replace('-', '_').upper()
            if name[0].isdigit():
                name = '_' + name
            w.write(f'{name} = chr(0x{unicode})\n')


main(HERE/'src/fontawesome47/icons_str.py')
