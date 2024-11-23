import tkinter as tk
import psutil

class TaskManagerFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        self.cpu_label = tk.Label(self, text="CPU Usage: ")
        self.cpu_label.pack(pady=5)

        self.memory_label = tk.Label(self, text="Memory Usage: ")
        self.memory_label.pack(pady=5)

    def update_status(self):
        self.cpu_label.config(text=f"CPU Usage: {psutil.cpu_percent()}%")
        memory = psutil.virtual_memory()
        self.memory_label.config(text=f"Memory Usage: {memory.percent}%")
        self.after(1000, self.update_status)
