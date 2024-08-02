import yaml

filename = '/home/poeticpotato/.config/qtile/settings.yml'

with open(filename, 'r') as file:
    settings = yaml.safe_load(file)

screen_settings = settings["screens"]

def save_settings():
    with open(filename, 'w') as file:
        yaml.dump(settings, file)
