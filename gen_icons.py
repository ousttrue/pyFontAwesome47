import pathlib

HERE = pathlib.Path(__file__).absolute().parent


def main(dst: pathlib.Path, is_bytes: bool):
    import fontawesome47.icons

    with dst.open('w') as w:
        for item in fontawesome47.icons.get_icons():
            unicode = item['unicode']
            name = item["id"].replace('-', '_').upper()
            if name[0].isdigit():
                name = '_' + name

            if is_bytes:
                w.write(f'{name} = b"\\u{unicode}"\n')
            else:
                w.write(f'{name} = "\\u{unicode}"\n')


main(HERE/'src/fontawesome47/icons_str.py', False)
main(HERE/'src/fontawesome47/icons_bytes.py', True)
