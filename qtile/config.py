# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor')
]

group_names = [
    "HOM",
    "CHR",
    "DEV",
    "DOC",
    "SC5",
    "SC6",
    "SC7"
    ]

groups = [Group(i) for i in group_names]

for i, group in enumerate(groups, 1):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(i),
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=["#4287f5"], border_normal=["#333333"], border_on_single=True, border_width=4, margin = 8),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Ubuntu Nerd Font',
    color='ebddbc',
    fontsize=15,
    padding=3
)
extension_defaults = widget_defaults.copy()

# https://coolors.co/000000-839788-eee0cb-baa898-bfd7ea
# bar_colors = ['222222', '839788', "EEE0CB", "BAA898"]
bar_colors = ['222222', '23395B', "8EA8C3", "CBF7ED"]
bar_groups = [bar_colors[1], bar_colors[2], bar_colors[3], bar_colors[1], bar_colors[2]]

def arrow_end(color, bg=bar_colors[0], flip=False):
    if flip:
        return widget.TextBox(
            text=' ❰',
            fontsize=45,
            foreground=color,
            background=bg,
            padding =-14
            )
    return widget.TextBox(
        text='❱ ',
        fontsize=60,
        foreground=color,
        background=bg,
        padding=-20
        )

def slice_end(color, bg=bar_colors[0]):
    return widget.TextBox(
        text='  ▲',
        fontsize=80,
        foreground=color,
        background=bg,
        padding = -48
        )

def group_space(color, width=10):
    return widget.Spacer(
        background=color,
        length=width)

bar1 = bar.Bar(
            [
                arrow_end(bar_groups[0], flip=True),
                widget.TextBox(
                    text="☔",
                    fontsize=20,
                    foreground=bar_groups[1],
                    background=bar_groups[0],
                    ),
                widget.GroupBox(
                    highlight_method='block',
                    hide_unused=False, 
                    inactive="999999",
                    max_chars=100,
                    active=widget_defaults["color"],
                    visible_groups=group_names[0:4],
                    background=bar_groups[0]),
                widget.Prompt(
                    font='Ubuntu Nerd Font',
                    foreground=widget_defaults["color"],
                    padding=8, 
                    background=bar_groups[0],
                    prompt='|   '),
                arrow_end(bar_groups[0], bar_groups[1]),
                widget.WindowName(
                    background=bar_groups[1],
                    width=bar.CALCULATED,
                    foreground="444444",
                    empty_group_string=""),
                group_space(bar_groups[1], width=14),
                arrow_end(bar_groups[1]),
                widget.Spacer(),
                slice_end(bar_groups[2]),
                group_space(bar_groups[2]),
                widget.TextBox(
                    text="Current Task: OStep Virtual Memory",
                    background=bar_groups[2],
                    foreground="444444",
                    width=bar.CALCULATED,
                    #foreground="170312",
                    ),
                slice_end(bar_groups[3], bar_groups[2]),
                group_space(bar_groups[3]),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p", 
                    background=bar_groups[3],
                    foreground=widget_defaults["color"],
                    #foreground="170312",
                    padding = 7),
                slice_end(bar_groups[4], bar_groups[3]),
                group_space(bar_groups[4]),
                widget.QuickExit(
                    default_text="POeticPotatoes",
                    foreground="444444",
                    background=bar_groups[4],),
                group_space(bar_groups[4])
            ],
            26,
            # border_width=[4, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["273b3d", "000000", "000000", "000000"],  # Borders are magenta
            background = bar_colors[0]
        )
bar2 = bar.Bar(
            [
                arrow_end(bar_groups[0], flip=True),
                widget.GroupBox(
                    highlight_method='block',
                    hide_unused=False, 
                    inactive="999999",
                    max_chars=100,
                    active=widget_defaults["color"],
                    visible_groups=group_names[4:7],
                    background=bar_groups[0]),
                widget.Prompt(
                    font='Ubuntu Nerd Font',
                    foreground=widget_defaults["color"],
                    padding=8, 
                    background=bar_groups[0],
                    prompt='|   '),
                arrow_end(bar_groups[0], bar_groups[1]),
                widget.WindowName(
                    background=bar_groups[1],
                    width=bar.CALCULATED,
                    foreground="444444",
                    empty_group_string=""),
                group_space(bar_groups[1], width=14),
                arrow_end(bar_groups[1]),
                widget.Spacer(),
                widget.TextBox(
                    text="\"Victory belongs to the most tenacious\"",
                    foreground=widget_defaults["color"],
                    width=290
                    ),
                slice_end(bar_groups[3]),
                group_space(bar_groups[3]),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p", 
                    background=bar_groups[3],
                    foreground=widget_defaults["color"],
                    #foreground="170312",
                    padding = 7),
                slice_end(bar_groups[4], bar_groups[3]),
                group_space(bar_groups[4]),
                widget.QuickExit(
                    default_text="POeticPotatoes",
                    foreground="444444",
                    background=bar_groups[4],),
                group_space(bar_groups[4])
            ],
            26,
            # border_width=[4, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["273b3d", "000000", "000000", "000000"],  # Borders are magenta
            background = bar_colors[0]
        )

screens = [
    Screen(bottom=bar1),
    Screen(bottom=bar2)
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
