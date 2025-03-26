# Gesture-Controlled-Virtual-Switch

Using the MediaPipeHands library from Google's MediaPipe framework to try and create a gesture-controlled switch that uses simple hand gestures to control something hardware (virtual for now) in Arduino

- using OpenCV + MediaPipe for real time hand-tracking and gesture-recognition
- possible applications for IoT, assistive technology, etc

### How It Works
- *Step 1*: Hand Gesture Recognition (Open Palm = ON, Fist = OFF).
- *Step 2*: Python sends '1' or '0' to Arduino via Serial Communication.
- *Step 3*: Arduino controls LED & Motor in Wokwi/Tinkercad Simulator.
