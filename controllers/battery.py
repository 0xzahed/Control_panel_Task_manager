import tkinter as tk
import psutil
import os

class BatteryFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.status_label = tk.Label(self, text="Fetching battery status...")
        self.status_label.pack(pady=10)

        shutdown_button = tk.Button(self, text="Shutdown", command=self.shutdown)
        shutdown_button.pack(pady=5)

        restart_button = tk.Button(self, text="Restart", command=self.restart)
        restart_button.pack(pady=5)

        # Call the update_battery_info function every 1000ms (1 second)
        self.update_battery_info()

    def update_battery_info(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            charging = battery.power_plugged
            status_text = f"Battery Percentage: {percent}%"
            if charging:
                status_text += " (Charging)"
            else:
                status_text += " (Not Charging)"
            self.status_label.config(text=status_text)
        else:
            self.status_label.config(text="Battery information not available.")

        # Refresh every 1 second (1000ms)
        self.after(1000, self.update_battery_info)

    def shutdown(self):
        os.system("shutdown now")

    def restart(self):
        os.system("reboot")
