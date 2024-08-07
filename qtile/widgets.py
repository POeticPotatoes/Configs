# from devicons import file_node_extensions
from libqtile import bar, widget, qtile
from theme import bar_colors, c1, c2, c3, widget_defaults
# from screens import singlescreen, doublescreen
from music_player import MusicPlayer
from gpu_display import GpuDisplay

def circle_end(color, bg=bar_colors[0], flip=False):
    if flip:
        return widget.TextBox(
            text='  ⚈',
            fontsize=35,
            foreground=color,
            background=bg,
            padding =-19
            )
    return widget.TextBox(
        text='  ',
        fontsize=35,
        foreground=color,
        background=bg,
        padding=-21
        )

def arrow_end(color, bg=bar_colors[0], flip=False):
    if flip:
        return widget.TextBox(
            text=' 🡸',
            fontsize=80,
            foreground=color,
            background=bg,
            padding =-22
            )
    return widget.TextBox(
        text='🡺   ',
        fontsize=80,
        foreground=color,
        background=bg,
        padding=-62
        )

def group_space(color, width=10):
    return widget.Spacer(
        background=color,
        length=width)

default_end = circle_end
application_color = bar_colors[2]

def widget_template(widget, color, left=None, right=None, right_color=None):
    if not right_color: right_color = color
    if left: widget = [default_end(color, left, True)] + widget
    if right: widget += [default_end(right_color, right)]
    return widget

def application(text, cmd, cmd2, font_size=15, font="None", color=application_color, font_color=c1, left=None, right=None, width=bar.CALCULATED):
    return widget_template([
                widget.TextBox(
                    text=text,
                    fontsize=font_size,
                    font=font,
                    width=width,
                    mouse_callbacks = {
                        'Button1': lambda: qtile.cmd_spawn(cmd),
                        'Button3': lambda: qtile.cmd_spawn(cmd2)},
                    background=color,
                    foreground=font_color,
                    padding=5
                ),
                group_space(color,2),
            ], color, left, right)

# Custom Widgets
def windowName(left=bar_colors[0], right=bar_colors[0]):
    color = bar_colors[1]
    return widget_template([
            widget.WindowName(
                width=bar.CALCULATED,
                padding=8, 
                font="Exo2 Regular",
                max_chars=60,
                background=color,
                foreground=c2,
                empty_group_string="Victory Belongs to the Most Tenacious"),
        ], color, left, right)

def musicPlayer(left=bar_colors[0], right=bar_colors[0]):
    color = bar_colors[2]
    return widget_template([
        MusicPlayer(
            padding=8, 
            font="Exo2 Regular",
            background=color,
            )
        ], color, left, right)
 
def gpuDisplay(left=bar_colors[0], right=bar_colors[0]):
    color = bar_colors[2]
    return widget_template([
        GpuDisplay(
            padding=8, 
            font="Exo2 Regular",
            background=color,
            )
        ], color, left, right)

symbols = ["🖧", "☣", "☔", "⛈", "", "", "", "", ""]
def homeBar(groups, max_chars=100, left=bar_colors[0], right=bar_colors[0]):
    color = [bar_colors[3],bar_colors[2]]
    return widget_template([
            widget.TextBox(
                text=symbols[6],
                fontsize=20,
                foreground=bar_colors[1],
                background=color[0],
                mouse_callbacks = {
                    'Button1': lambda: qtile.cmd_spawn("alacritty -e repo")},
                padding=10
                ),
            widget.GroupBox(
                highlight_method='line',
                hide_unused=False, 
                inactive=c3,
                active=c1,
                font="Exo2 Regular",
                highlight_color=bar_colors[5],
                disable_drag=True,
                max_chars=max_chars,
                visible_groups=groups,
                background=color[0]),
        ], color[0], left, right)

def prompt(left=bar_colors[0], right=bar_colors[0]):
    color = bar_colors[2]
    return widget_template([
            widget.Prompt(
                padding=8, 
                background=color,
                prompt=':   '),
            group_space(color,10),
        ], color, left, right)

def soundbar(left=bar_colors[0], right=bar_colors[0]):
    color = [bar_colors[1], bar_colors[2]]
    return (application(
                "",
                "setaudio Samson_G-Track_Pro",
                "", 
                color=color[0], font_color=c2, font_size=18, left=left,right=None)
            + [group_space(color[0], width=5)]
            + [group_space(color[1], width=3)]
            + application(
                "蓼",
                "setaudio HiFi__hw_Audio__sink",
                "",
                color=color[1], font_size=20, left=None, right=right))

def clock(left=bar_colors[0], right=bar_colors[0]):
    color = bar_colors[3]
    return widget_template([
            widget.Clock(
                format="%Y-%m-%d %a %I:%M %p", 
                background=color,
                font="Exo2 Regular",
                padding = 12),
        ], color, left, right)

def power_button(text="POeticPotatoes", left=bar_colors[0], right=bar_colors[0]):
    color = bar_colors[2]
    return widget_template([
            widget.QuickExit(
                default_text=text,
                background=color,
                font="Exo2 Regular",
                foreground=widget_defaults["color"],
                countdown_format="[{} seconds]     ",
                padding=14),
        ], color, left, right)

def brightness(left=bar_colors[0], right=bar_colors[0], screen=""):
    color = [bar_colors[1], bar_colors[4], bar_colors[3]]
    return (application(
                " ",
                f'brightness {screen} 1',
                "", 
                color=color[0], font_size=20, left=left,right=None)
            + application(
                " 🌣",
                f'brightness {screen} 0.7',
                " ",
                color=color[1], font_size=20, left=None, right=None)
            + application(
                "   ",
                f'brightness {screen} 0.5',
                "",
                color=color[2], font_size=20, left=None, right=right))

# Applications
# Bros designed to look good when chained

applications = {
        'nitrogen': ("", "nitrogen", "randomwallpaper"),
        'telegram': ("", "xdg-open https://web.telegram.org", ""),
        'discord': ("ﭮ", "xdg-open https://discord.com/app", "",20),
        'whatsapp': ("", "xdg-open https://web.whatsapp.com", "",20),
        'doublescreen': ("⚉", "custominit", "",20),
        'singlescreen': ("⚈", "bedview", "",20),
        'translate': ("", "xdg-open https://translate.google.com", "",20),
        'codeforces': ("C", "xdg-open https://codeforces.com/submissions/POeticPotato", "",20),
        }

def application_bar(apps, left=bar_colors[0], right=bar_colors[0]):
    bar = []
    for i in apps:
        bar += application(*applications[i], left=None, right=None,
                        font="Agave Nerd Font", width=35)
    return widget_template(bar, application_color, left=left, right=right)
