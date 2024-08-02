import subprocess
from libqtile import qtile
from settings import screen_settings, save_settings

def switch_group(index, screen):
    def f(qtile):
        if (screen_settings["force-switch-screen"]): qtile.cmd_to_screen(screen)
        qtile.current_screen.set_group(qtile.groups[index])
    return f;

def change_group(group, index, screen):
    def f(qtile):
        qtile.current_window.togroup(group)
        if (screen_settings["force-switch-screen"]): qtile.cmd_to_screen(screen)
        qtile.current_screen.set_group(qtile.groups[index])
    return f;

def singlescreen():
    screen_settings["force-switch-screen"] = False
    screen_settings["force-show-groups"] = True
    save_settings()
    qtile.cmd_spawn("bedview")

def doublescreen():
    screen_settings["force-switch-screen"] = True
    screen_settings["force-show-groups"] = False
    save_settings()
    qtile.cmd_spawn("custominit")
