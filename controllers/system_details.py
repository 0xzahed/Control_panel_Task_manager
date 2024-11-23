import tkinter as tk
import platform
import psutil
import shutil
from datetime import datetime

class SystemDetailsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="white")  # Set the background to white

        title_label = tk.Label(
            self, text="System Details", font=("Arial", 18, "bold"), fg="black", bg="white"
        )
        title_label.pack(pady=20)

        # Buttons for additional options (Date & Time, User, SSH, About, Software Updates)
        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(fill="x", pady=20)

        date_time_button = tk.Button(button_frame, text="Date & Time", command=self.show_date_time)
        date_time_button.grid(row=0, column=0, padx=10)

        user_button = tk.Button(button_frame, text="User Info", command=self.show_user_info)
        user_button.grid(row=0, column=1, padx=10)

        ssh_button = tk.Button(button_frame, text="Secure Shell", command=self.show_secure_shell)
        ssh_button.grid(row=0, column=2, padx=10)

        about_button = tk.Button(button_frame, text="About", command=self.show_about)
        about_button.grid(row=0, column=3, padx=10)

        updates_button = tk.Button(button_frame, text="Software Updates", command=self.show_software_updates)
        updates_button.grid(row=0, column=4, padx=10)

        # Placeholder label to show the content when buttons are clicked
        self.content_label = tk.Label(self, text="", font=("Arial", 12), fg="black", bg="white")
        self.content_label.pack(pady=10)

    def show_about(self):
        """ Show system details under the About section """
        about_text = (
            f"OS: {platform.system()} {platform.release()} ({platform.version()})\n"
            f"Processor: {platform.processor()}\n"
            f"Memory: {round(psutil.virtual_memory().total / (1024 ** 3), 1)} GiB\n"
            f"Disk Capacity: {self.get_disk_capacity()}\n"
            f"Machine Name: {platform.node()}"
        )
        self.content_label.config(text=f"About the System:\n{about_text}")

    def show_date_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.content_label.config(text=f"Current Date & Time: {current_time}")

    def show_user_info(self):
        user_info = platform.uname()
        self.content_label.config(text=f"User Info: {user_info.node} ({user_info.system} {user_info.release})")

    def show_secure_shell(self):
        # Check if SSH is enabled
        # This is a placeholder; adjust based on your SSH configuration method
        try:
            # Assuming SSH is enabled if port 22 is open
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', 22))
                self.content_label.config(text="SSH is enabled")
        except Exception:
            self.content_label.config(text="SSH is not enabled")

    def show_software_updates(self):
        # Placeholder for software updates functionality
        self.content_label.config(text="Checking for software updates... (This is a placeholder)")

    def get_disk_capacity(self):
        """ Method to get total disk capacity """
        total, used, free = shutil.disk_usage("/")
        return f"{round(total / (1024 ** 3), 1)} GiB"
