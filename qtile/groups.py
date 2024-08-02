from libqtile.config import Group
from settings import screen_settings

group_names = [[
    "HOM",
    "FRF",
    "DEV",
    ],[
    "SC4",
    "SC5",
    "SC6",
    "QPW",
    ]]

groups = [Group(n) for g in group_names for n in g]

def get_groups(id):
    if (screen_settings["force-show-groups"]): return [n for g in group_names for n in g]
    return group_names[id]
