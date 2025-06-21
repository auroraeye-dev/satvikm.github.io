import pyautogui
import time

# print("Looking for Skip Ad button...")
# image_path = r"file path"  # Adjust if needed

# start = time.time()
# match = None
# while time.time() - start < 15:
#     match = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
#     if match:
#         print(f"Button found at: {match}")
#         pyautogui.moveTo(match.x, match.y)
#         pyautogui.click()
#         print("Clicked the Skip Ad button.")
#         break
#     else:
#         print("Not found yet...")
#     time.sleep(1)

# if not match:
#     print("No match found in 15 seconds.")

def try_skip_ad(image_path, timeout=15):
    print("Looking for Skip Ad button...")
    start = time.time()
    match = None
    while time.time() - start < timeout:
        try:
            match = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
        except pyautogui.ImageNotFoundException:
            print("Skip Ad button not found in current frame.")
            match = None

        if match:
            print(f"Skip Ad found at {match}. Clicking...")
            pyautogui.moveTo(match)
            pyautogui.click()
            break
        else:
            print("Not found yet... retrying")
        time.sleep(1)

    if not match:
        print("No Skip Ad button found after 15 seconds. Carrying on...")
try_skip_ad(r"file_path")
