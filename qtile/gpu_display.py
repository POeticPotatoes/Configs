from datetime import datetime
import os

from libqtile.widget import base

class GpuDisplay(base.ThreadPoolText):

    defaults = [
        ("play_icon", "▶", "icon to display when playing music"),
        ("pause_icon", "", "icon to display when music paused"),
        ("update_interval", 0.5, "polling rate in seconds"),
        ("format", "{icon}     {song_title}", "Spotify display format"),
    ]

    paused = True
    loaded = False
    started = False

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, text="", **config)
        base.ThreadPoolText.__init__(self, text="", **config)

    def poll(self):
        val = os.popen("nvidia-settings -q gpucoretemp | grep Attribute").read()
        return val[-6:].partition('\n')[0] + datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    v = GpuDisplay()
    print(v.poll())
