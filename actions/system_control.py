import pyautogui
import json
import os

# Load config mapping
config_path = os.path.join("config", "mapping.json")
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        gesture_map = json.load(f)
else:
    gesture_map = {
        "Right": {
            "1": "space",
            "2": "nexttrack",
            "3": "volumedown",
            "4": "volumeup",
            "5": "volumemute"
        }
    }

def perform_action(finger_count, hand_label):
    hand_map = gesture_map.get(hand_label, gesture_map.get("Right"))
    key = str(finger_count)
    if key in hand_map:
        pyautogui.press(hand_map[key])
        return hand_map[key].capitalize()
    return None
