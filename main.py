import tkinter as tk
from tkinter import ttk
from controllers import network, sound, battery, system_monitor, system_details, SystemSecurity

class PyOSManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Manager")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")

        self.current_frame = None
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Control Panel", font=("Arial", 24, "bold"), bg="#ffffff")
        title_label.pack(pady=20)

        # Navigation Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(side="top", fill="x", pady=10)

        network_button = tk.Button(button_frame, text="Network Settings", command=self.show_network_frame)
        network_button.grid(row=0, column=0, padx=5)

        sound_button = tk.Button(button_frame, text="Sound Settings", command=self.show_sound_frame)
        sound_button.grid(row=0, column=1, padx=5)

        battery_button = tk.Button(button_frame, text="Battery Status", command=self.show_battery_frame)
        battery_button.grid(row=0, column=2, padx=5)

        task_manager_button = tk.Button(button_frame, text="Task Manager", command=self.show_task_manager_frame)
        task_manager_button.grid(row=0, column=3, padx=5)

        system_details_button = tk.Button(button_frame, text="System Details", command=self.show_system_details_frame)
        system_details_button.grid(row=0, column=4, padx=5)

        # New System & Security Button
        system_security_button = tk.Button(button_frame, text="System & Security", command=self.show_system_security_frame)
        system_security_button.grid(row=0, column=5, padx=5)

        # Content Frames
        self.network_frame = network.NetworkFrame(self.root)
        self.sound_frame = sound.SoundFrame(self.root)
        self.battery_frame = battery.BatteryFrame(self.root)
        self.task_manager_frame = system_monitor.TaskManagerFrame(self.root)
        self.system_details_frame = system_details.SystemDetailsFrame(self.root)
        self.system_security_frame = SystemSecurity.SystemSecurityFrame(self.root)

        # Show the initial frame (e.g., Network Frame)
        self.show_network_frame()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack(expand=True, fill="both")

    def show_network_frame(self):
        self.show_frame(self.network_frame)

    def show_sound_frame(self):
        self.show_frame(self.sound_frame)

    def show_battery_frame(self):
        self.show_frame(self.battery_frame)

    def show_task_manager_frame(self):
        self.show_frame(self.task_manager_frame)

    def show_system_details_frame(self):
        self.show_frame(self.system_details_frame)

    def show_system_security_frame(self):
        self.show_frame(self.system_security_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = PyOSManagerApp(root)
    root.mainloop()
