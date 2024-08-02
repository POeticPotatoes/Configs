from libqtile.group import _Group
from libqtile.config import Screen

from libqtile.widget import base
from threading import Thread
import osu_loader
import mpv

class MusicPlayer(base.ThreadPoolText):

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
        self.player = mpv.MPV(ytdl=True)
        self.player.command("set", "volume", "50")
        base.ThreadPoolText.__init__(self, text="", **config)
        self.add_defaults(MusicPlayer.defaults)
        self.add_callbacks({
            "Button1": self.toggle_music,
            "Button2": self.kill_music,
            "Button3": self.skip_music,
            "Button4": self.volume_down,
            "Button5": self.volume_up
            })
        thread = Thread(target=self.load_songs)
        thread.start()

    def __del__(self):
        self.kill_music()

    def load_songs(self):
        playlist = osu_loader.obtain_playlist()
        for song in playlist:
            self.player.playlist_append(song)
        self.loaded = True

    def toggle_music(self):
        if not self.player: return
        if not self.started:
            self.player.playlist_play_index(1)
            self.started=True
            self.paused=False
        else:
            self.player.cycle("pause")
            self.paused = not self.paused

    def skip_music(self):
        if not self.player: return
        self.player.playlist_next()

    def kill_music(self):
        if not self.player: return
        self.player.terminate()
        self.player = None

    def volume_up(self):
        self.player.property_add("volume", 5)

    def volume_down(self):
        self.player.property_add("volume", -5)

    def poll(self):
        if not self.player: return "Unloaded"
        vars = {
            "icon": "⌛" if not self.loaded else self.play_icon if self.paused else self.pause_icon,
            "artist": self.artist,
            "song_title": self.song_title,
        }
        return self.format.format(**vars)

    def limit(self, s, length):
        return s if len(s)<=length else f'{s[:length-2]}..'

    @property
    def artist(self) -> str:
        properties = self.player._get_property("filtered-metadata")
        return self.limit(properties['Artist'], 20) if properties and 'Artist' in properties else "Unknown"

    @property
    def song_title(self) -> str:
        properties = self.player._get_property("filtered-metadata")
        return self.limit(properties['Title'], 20) if properties and 'Artist' in properties else "Unknown"
