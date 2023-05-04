from libqtile.config import Key, Drag, Click, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from groups import groups, group_names
from widgets import applications

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
    Key(["mod1"], "tab", lazy.layout.next(), desc="Move window focus to other window"),
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
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key( [mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "r", lazy.spawn("alacritty -e repo"), desc="Open a github repository"),
    Key([], "Print", lazy.spawn("scrot /home/poeticpotato/screenshots/%Y-%m-%d-%T-screenshot.png")),
    Key(["shift"], "Print", lazy.spawn("import /home/poeticpotato/screenshots/area.png")),
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),
    Key([mod], "f", lazy.window.toggle_floating(), desc='Toggle floating')
]

def switch_group(index, screen):
    def f(qtile):
        qtile.cmd_to_screen(screen)
        qtile.current_screen.set_group(qtile.groups[index])
    return f;

def change_group(group, index, screen):
    def f(qtile):
        qtile.current_window.togroup(group)
        qtile.cmd_to_screen(screen)
        qtile.current_screen.set_group(qtile.groups[index])
    return f;

i = 0;
for s, gg in enumerate(group_names):
    for g in gg:
        keys.extend(
            [
                Key( [mod], str(i+1),
                    lazy.function(switch_group(i, s)),
                    desc="Switch to group {}".format(g),
                ),
                Key( [mod, "shift"], str(i+1),
                    lazy.function(change_group(g, i, s)),
                    desc="Switch to & move focused window to group {}".format(g),
                ),
            ]
        )
        i += 1

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

def bind_applications(apps):
    global keys
    a = []
    for i, app in enumerate(apps,1):
        a.extend([
            Key([], str(i), 
                lazy.spawn(applications[app][1]),
                desc="Open {}".format(app),
                )])
    keys.extend([KeyChord([mod], "a", a)])
