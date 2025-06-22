import mediapipe as mp
import cv2

class HandGestureDetector:
    def __init__(self, max_hands=1, detection_confidence=0.9):
        self.hands_module = mp.solutions.hands
        self.hands = self.hands_module.Hands(max_num_hands=max_hands, min_detection_confidence=detection_confidence)
        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame_rgb, frame_bgr):
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                hand_label = hand_info.classification[0].label  # 'Left' or 'Right'
                finger_count = self.count_fingers(hand_landmarks, hand_label)
                self.drawer.draw_landmarks(frame_bgr, hand_landmarks, self.hands_module.HAND_CONNECTIONS)
                return finger_count, hand_label
        return None

    def count_fingers(self, landmarks, label):
        fingers = []

        # Thumb (different direction for left vs right hand)
        if label == "Right":
            fingers.append(1 if landmarks.landmark[4].x < landmarks.landmark[3].x else 0)
        else:
            fingers.append(1 if landmarks.landmark[4].x > landmarks.landmark[3].x else 0)

        # Other 4 fingers
        tip_ids = [8, 12, 16, 20]
        for tip_id in tip_ids:
            fingers.append(1 if landmarks.landmark[tip_id].y < landmarks.landmark[tip_id - 2].y else 0)

        return sum(fingers)
