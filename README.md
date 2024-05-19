# LuminarHand - Hand Gesture Controlled Screen Brightness

This project utilizes OpenCV, MediaPipe, and `screen_brightness_control` to adjust screen brightness based on the distance between the thumb and index finger detected in real-time via a webcam. By moving your thumb and index finger closer or farther apart, you can dynamically control the brightness of your screen.

## Requirements

- Python 3.6 or higher
- OpenCV
- MediaPipe
- NumPy
- screen_brightness_control

# Initial Setup:

- Initialize MediaPipe hands solution.
- Capture video from the webcam.
- Set the width and height of the video frame.

## Main Loop:

- Capture a frame from the webcam.
- Convert the frame to RGB for MediaPipe processing.
- Process the frame to detect hands.
- Extract hand landmarks if any are detected.

## Processing Detected Hands:

- Draw hand landmarks on the frame.
- Iterate through each landmark in the hand.
- Convert normalized landmark coordinates to pixel coordinates.
- If the landmark is the thumb tip or index finger tip, draw a circle at the coordinates.
- Calculate the distance between the thumb and index finger tips.
- Map the distance to a brightness value using np.interp.
- Set the screen brightness using sbc.set_brightness.

## FPS Calculation and Display:

- Calculate the frame rate.
- Display the frame rate on the frame.
- Show the frame.
- Exit the loop if 'x' is pressed.
