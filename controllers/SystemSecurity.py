import tkinter as tk
import psutil
import os
from tkinter import ttk


class SystemSecurityFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self, text="System & Security", font=("Arial", 18, "bold"), fg="black", bg="white")
        title_label.pack(pady=20)

        # System Information
        system_info_frame = tk.Frame(self, bg="white")
        system_info_frame.pack(fill="x", padx=20, pady=10)

        # CPU Usage
        cpu_label = tk.Label(system_info_frame, text=f"CPU Usage: {psutil.cpu_percent()}%", font=("Arial", 12), fg="black", bg="white")
        cpu_label.pack(anchor="w", padx=10)

        # Memory Usage
        memory = psutil.virtual_memory()
        memory_label = tk.Label(system_info_frame, text=f"Memory Usage: {round(memory.percent, 2)}%", font=("Arial", 12), fg="black", bg="white")
        memory_label.pack(anchor="w", padx=10)

        # Disk Usage
        disk = psutil.disk_usage('/')
        disk_label = tk.Label(system_info_frame, text=f"Disk Usage: {round(disk.percent, 2)}%", font=("Arial", 12), fg="black", bg="white")
        disk_label.pack(anchor="w", padx=10)

        # Security Section (for example: firewall status)
        firewall_status = self.get_firewall_status()
        firewall_label = tk.Label(self, text=f"Firewall Status: {firewall_status}", font=("Arial", 12), fg="black", bg="white")
        firewall_label.pack(pady=10)

        # SSH Toggle Button (for example: enabling/disabling SSH)
        ssh_button = tk.Button(self, text="Enable SSH", command=self.toggle_ssh)
        ssh_button.pack(pady=5)

    def get_firewall_status(self):
        """ Example function to check firewall status (assuming UFW is installed) """
        try:
            result = os.popen('sudo ufw status').read()
            return "Active" if "Status: active" in result else "Inactive"
        except Exception as e:
            return "Error: " + str(e)

    def toggle_ssh(self):
        """ Function to enable or disable SSH """
        # Example: Check if SSH is running, and toggle
        if os.system("systemctl is-active --quiet ssh"):
            os.system("sudo systemctl stop ssh")  # Disable SSH
            os.system("sudo systemctl disable ssh")
        else:
            os.system("sudo systemctl enable ssh")  # Enable SSH
            os.system("sudo systemctl start ssh")


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

        system_security_button = tk.Button(button_frame, text="System & Security", command=self.show_system_security_frame)
        system_security_button.grid(row=0, column=5, padx=5)

        # Content Frames
        self.network_frame = tk.Frame(self.root)
        self.sound_frame = tk.Frame(self.root)
        self.battery_frame = tk.Frame(self.root)
        self.task_manager_frame = tk.Frame(self.root)
        self.system_details_frame = tk.Frame(self.root)
        self.system_security_frame = SystemSecurityFrame(self.root)

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
