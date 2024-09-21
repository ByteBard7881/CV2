import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import mss

def basic():
    img = cv2.imread('./back.jpg') # Load image
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # Resize image
    cv2.imshow('Image', img) # Show image
    # Wait for infinite amount of time for a key to press and terminate image show
    cv2.waitKey(0)
    cv2.destroyAllWindows() # Destroy window

def video_stream():
    # Attempt to access the camera, handle potential failure
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("[-] Could not open video device.")
            return
    except Exception as e:
        print(f"[-] Error initializing video capture: {e}")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Check if frame capture was successful
        if not ret:
            print("[-] Failed to capture frame. Exiting...")
            break

        try:
            # Resize the frame and display it
            frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
            cv2.imshow('frame', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(1) == ord('q'):
                break
        except Exception as e:
            print(f"[-] Exception during frame processing: {e}")
            break

    # Release resources properly
    cap.release()
    cv2.destroyAllWindows()
    
def screen_share_pyautogui():
    while True:
        img = pyautogui.screenshot() # Capture the screen
        frame = np.array(img) # Convert image to numpy array
        # Convert RGB to BGR (OpenCV uses BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # Resize the frame and display it
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Screen Capture", frame) # Display the frame
        if cv2.waitKey(1) == ord('q'):
            print("[+] Exit key pressed. Exiting...")
            break
    # Release resources properly
    cv2.destroyAllWindows()
    
def screen_share_pillow():
    while True:
        img = ImageGrab.grab() # Capture the screen
        frame = np.array(img) # Convert image to numpy array
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # Resize the frame and display it
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Screen Capture", frame) # Display the frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release resources properly
    cv2.destroyAllWindows()
    
def screen_share_mss():
    with mss.mss() as sct:
        # Get the size of the primary monitor
        monitor = sct.monitors[1]  # 1 is the primary monitor\
        while True:
            # Capture the screen
            img = sct.grab(monitor)
            # Convert to numpy array
            frame = np.array(img)
            # Convert BGRA to BGR (remove alpha channel)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            # Resize the frame and display it
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            # Display the frame
            cv2.imshow("Screen Capture", frame)
            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # Release resources properly
    cv2.destroyAllWindows()

if __name__ == '__main__':
    pass