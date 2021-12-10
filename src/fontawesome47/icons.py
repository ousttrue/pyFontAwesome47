ICONS = 'fonts/icons.yml'


def get_icons():
    import pkgutil
    data = pkgutil.get_data('fontawesome47', ICONS)
    if not data:
        raise Exception(f'{ICONS} not found')
    import yaml
    return yaml.safe_load(data)['icons']
