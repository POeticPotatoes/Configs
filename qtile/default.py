from libqtile import bar, layout, widget, hook
from libqtile.config import Match, Screen
from theme import bar_colors
from keybinds import groups, keys, mouse, mod, bind_applications
from groups import get_groups
from settings import screen_settings
from theme import widget_defaults
import os, subprocess

layouts = [
    layout.Columns(border_focus=["#8EA8C3"], border_normal=["#333333"], grow_amount=14, border_on_single=True, border_width=0, margin = 11),
    layout.Floating(border_focus=["#8EA8C3"], border_normal=["#333333"], grow_amount=14, border_on_single=True, border_width=1, margin = 11),
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    layout.VerticalTile(border_focus=["#8EA8C3"], border_normal=["#333333"], grow_amount=14, border_on_single=True, border_width=0, margin = 11),
    # layout.Zoomy(),
]

widget_defaults = widget_defaults
extension_defaults = widget_defaults.copy()

@hook.subscribe.startup_complete
def call_custominit():
    home = os.path.expanduser("/usr/local/bin/custominit")
    subprocess.call([home])

applications = ["whatsapp", "telegram", "nitrogen"]
bind_applications(applications)

bar1 = bar.Bar(
        [widget.Spacer()]
        # [widgets.group_space(bar_colors[3])]
        # widgets.application_bar(applications)
        # + widgets.screen_select()
        # + widgets.brightness(screen=screen_settings["main-screen"])
        # + [widget.Spacer()]
        # + widgets.homeBar(get_groups(0), right=None)
        # + widgets.windowName(right=bar_colors[2], left=bar_colors[3])
        # + widgets.prompt(left=None)
        # + [widget.Spacer()]
        # + widgets.musicPlayer()
        # + widgets.clock(right=None)
        # + widgets.power_button(left=bar_colors[3], right=None)
        ,
        26,
        background = bar_colors[0],
        margin = [13, 0, 0, 0])

bar2 = bar.Bar(
        #widgets.brightness(screen="HDMI-0")
        [widget.Spacer()]
        #+ widgets.homeBar(get_groups(1), max_chars=20, right=None)
        #+ widgets.windowName(left=bar_colors[3])
        #+ [widget.Spacer(length=370)]
        #+ [widget.Spacer()]
        ,
        26,
        background = bar_colors[0],
        margin = [13, 0, 0, 0])

screens = [Screen(top=bar1), Screen(top=bar2)]

# Drag floating layouts.
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=["#8EA8C3"],
    border_normal=["333333"],
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
focus_on_window_activation = "never"
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
