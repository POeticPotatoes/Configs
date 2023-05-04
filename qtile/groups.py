from libqtile.config import Group

group_names = [[
    "HOM",
    "CHR",
    "DOC",
    "MUS",
    ],[
    "SC5",
    "SC6",
    "SC7"
    ]]

groups = [Group(i) for g in group_names for i in g]

