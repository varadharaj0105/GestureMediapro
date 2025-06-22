from hands.detector import HandGestureDetector
from actions.system_control import perform_action
from utils.helper import cooldown_passed, update_last_time
import cv2
import time

detector = HandGestureDetector()
prev_action = ""
last_trigger_time = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_info = detector.detect(rgb, frame)

    if hand_info:
        finger_count, hand_label = hand_info
        if cooldown_passed(last_trigger_time):
            action = perform_action(finger_count, hand_label)
            if action:
                prev_action = action
                last_trigger_time = update_last_time()

        cv2.putText(frame, f"Gesture: {prev_action}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

    cv2.imshow("GestureMediaPro", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
