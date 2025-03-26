import serial
import mediapipe as mp
import serial
import time

arduino= serial.Serial('COM3, 9600')
time.sleep(5)

#initializing hand tracking

handsutil = mp.solutions.hands
draw = mp.solutions.drawing_utils
hands = handsutil.Hands(min_detetction_confidenc=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    detected = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

            if index_tip < thumb_tip:  # Open Palm means on
                detected = '1'
                cv2.putText(frame, "ON", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:  # Fist means off
                detected = '0'
                cv2.putText(frame, "OFF", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            if detected:
                arduino.write(detected.encode())  # 1 or 0 output

    cv2.imshow("Hand-Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
