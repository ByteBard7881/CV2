# CV2

This repository contains code for basic image display, video streaming from a webcam, and different methods for screen capture using `pyautogui`, `Pillow`, and `mss` libraries.

## Directory Structure
```
_CODE/
    img.jpg       # An example image used for the 'basic' function
    main.py        # The main Python script with various functionalities
```

## Getting Started
To get started with this project, clone the repository and install the required libraries.

### Prerequisites
You need to have Python installed. The required libraries can be installed using:
```bash
pip install opencv-python numpy pyautogui Pillow mss
```

## Explanation of `main.py`
The `main.py` script provides various functionalities to display images, video streams, and screen sharing.

### Import Statements
```python
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import mss
```
These libraries are used for handling image and video capture, manipulation, and display.

### Functions

#### 1. `basic()`
- **Purpose**: Loads and displays the `img.jpg` image.
- **Process**:
  - Loads `img.jpg` using OpenCV.
  - Resizes the image to 50% of its original size.
  - Displays the image until a key is pressed.

#### 2. `video_stream()`
- **Purpose**: Streams video from the computer's webcam.
- **Process**:
  - Opens a connection to the webcam using OpenCV.
  - Captures frames continuously and displays them in a window.
  - Press 'q' to exit the stream.

#### 3. `screen_share_pyautogui()`
- **Purpose**: Shares the screen using the `pyautogui` library.
- **Process**:
  - Continuously captures the screen using `pyautogui.screenshot()`.
  - Converts the captured screenshot into a NumPy array and displays it using OpenCV.
  - Press 'q' to stop screen sharing.

#### 4. `screen_share_pillow()`
- **Purpose**: Shares the screen using the `Pillow` library (`ImageGrab`).
- **Process**:
  - Uses `ImageGrab.grab()` to capture the screen.
  - Converts the captured image into a NumPy array and displays it.
  - Press 'q' to stop screen sharing.

#### 5. `screen_share_mss()`
- **Purpose**: Shares the screen using the `mss` library for better performance.
- **Process**:
  - Captures the screen using `mss`.
  - Converts the captured image into a NumPy array and displays it.
  - Press 'q' to stop screen sharing.

### Usage
To run any of these functions, modify the `if __name__ == '__main__':` block in `main.py` as follows:

```python
if __name__ == '__main__':
    basic()                # To display the img.jpg image
    video_stream()         # To stream video from the webcam
    screen_share_pyautogui()  # To share screen using pyautogui
    screen_share_pillow()     # To share screen using Pillow
    screen_share_mss()        # To share screen using mss
```

### Notes
- Ensure your webcam is connected if using `video_stream()`.
- Press 'q' to exit any of the screen capture or video streaming functions.