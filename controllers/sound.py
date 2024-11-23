import tkinter as tk
import alsaaudio

class SoundFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.mixer = alsaaudio.Mixer()
        self.create_widgets()

    def create_widgets(self):
        volume_label = tk.Label(self, text="Volume:")
        volume_label.pack()

        self.volume_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(self.mixer.getvolume()[0])
        self.volume_slider.pack()

    def set_volume(self, vol):
        self.mixer.setvolume(int(vol))
