import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

config_path = os.path.join("config", "mapping.json")
default_actions = ["space", "nexttrack", "prevtrack", "volumeup", "volumedown", "volumemute", "playpause", "none"]

class GestureGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gesture Mapping")
        self.root.geometry("500x400")

        self.hand_options = ["Right", "Left"]
        self.gesture_entries = {}

        self.load_mapping()
        self.create_widgets()

    def load_mapping(self):
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                self.gesture_map = json.load(f)
        else:
            self.gesture_map = {"Right": {}, "Left": {}}

    def save_mapping(self):
        for hand in self.hand_options:
            for i in range(1, 6):
                action = self.gesture_entries[hand][i].get()
                if hand not in self.gesture_map:
                    self.gesture_map[hand] = {}
                self.gesture_map[hand][str(i)] = action

        with open(config_path, "w") as f:
            json.dump(self.gesture_map, f, indent=2)
        messagebox.showinfo("Saved", "Gesture mappings saved successfully!")

    def create_widgets(self):
        row = 0
        for hand in self.hand_options:
            tk.Label(self.root, text=f"{hand} Hand", font=("Arial", 12, "bold")).grid(row=row, column=0, columnspan=2, pady=(10, 0))
            row += 1

            self.gesture_entries[hand] = {}

            for i in range(1, 6):
                tk.Label(self.root, text=f"{i} Finger(s):").grid(row=row, column=0, padx=10, pady=5, sticky="e")

                selected_action = tk.StringVar()
                selected_action.set(self.gesture_map.get(hand, {}).get(str(i), "none"))

                combo = ttk.Combobox(self.root, textvariable=selected_action, values=default_actions, state="readonly")
                combo.grid(row=row, column=1, padx=10, pady=5)
                self.gesture_entries[hand][i] = selected_action

                row += 1

        tk.Button(self.root, text="Save", command=self.save_mapping, bg="#4CAF50", fg="white", width=20).grid(row=row, column=0, columnspan=2, pady=20)

def launch_gui():
    root = tk.Tk()
    app = GestureGUI(root)
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
