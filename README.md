# Gesture-Controlled-Virtual-Switch

Using the MediaPipeHands library from Google's MediaPipe framework to try and create a gesture-controlled switch that uses simple hand gestures to control something hardware (virtual for now) in Arduino

- using OpenCV + MediaPipe for real time hand-tracking and gesture-recognition
- possible applications for IoT, assistive technology, etc

### How It Works
- *Step 1*: Hand Gesture Recognition (Open Palm = ON, Fist = OFF).
- *Step 2*: Python sends '1' or '0' to Arduino via Serial Communication.
- *Step 3*: Arduino controls LED & Motor in Wokwi/Tinkercad Simulator.

### Future Improvements & Extensions

- Multi-Gesture Recognition

    Extend beyond simple on/off gestures to include more complex commands (e.g., swipe left/right for volume control, pinch for zoom).
    Implement dynamic gestures (e.g., drawing in the air to trigger actions).

- Wireless Connectivity (IoT Integration)

    Replace USB Serial communication with Bluetooth (HC-05), Wi-Fi (ESP8266/ESP32), or MQTT for remote control.
    Control IoT devices like lights, fans, or smart appliances via hand gestures.

- Cross platform support
