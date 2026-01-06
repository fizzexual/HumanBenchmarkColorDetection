import pyautogui
from PIL import ImageGrab
import time

TARGET_COLOR = (75, 219, 106)  
CLICK_DELAY_MS = 1  

def get_mouse_color():
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    screen_width, screen_height = screen.size

    if 0 <= x < screen_width and 0 <= y < screen_height:
        return screen.getpixel((x, y)), (x, y)
    else:
        return None, (x, y)

def main():
    click_delay_seconds = CLICK_DELAY_MS / 1000.0 
    print(f"Move your mouse. Program will wait {CLICK_DELAY_MS} ms before clicking when color {TARGET_COLOR} is detected.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            color, position = get_mouse_color()
            if color is not None:
                if color == TARGET_COLOR:
                    print(f"Detected color {TARGET_COLOR} at {position}. Waiting {CLICK_DELAY_MS} ms before clicking...")
                    time.sleep(click_delay_seconds) 
                    pyautogui.click(position)
                    print(f"Clicked at {position}.")
            else:
                print(f"Mouse out of bounds at position {position}.")
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
