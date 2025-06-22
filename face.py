import cv2
import mediapipe as mp
import pyautogui
import time

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.9)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_action = ""
last_trigger_time = 0

def count_fingers(hand_landmarks):
    fingers = []

    # Thumb detection
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    if thumb_tip.x < thumb_ip.x:  # Adjust for right hand
        fingers.append(1)
    else:
        fingers.append(0)

    # Index to Pinky
    tip_ids = [8, 12, 16, 20]
    for tip_id in tip_ids:
        tip = hand_landmarks.landmark[tip_id]
        pip = hand_landmarks.landmark[tip_id - 2]
        if tip.y < pip.y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            finger_count = count_fingers(handLms)
            now = time.time()

            if now - last_trigger_time > 1.2:
                if finger_count == 1:
                    pyautogui.press("space")
                    prev_action = "Pause/Play"
                elif finger_count == 2:
                    pyautogui.press("nexttrack")
                    prev_action = "Next Track"
                elif finger_count == 3:
                    pyautogui.press("volumedown")
                    prev_action = "Volume Down"
                elif finger_count == 4:
                    pyautogui.press("volumeup")
                    prev_action = "Volume Up"
                elif finger_count == 5:
                    pyautogui.press("volumemute")
                    prev_action = "Mute"

                last_trigger_time = now

            # Display info
            cv2.putText(frame, f"Gesture: {prev_action}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
            cv2.putText(frame, f"Fingers: {finger_count}", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)

    cv2.imshow("Gesture Media Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
