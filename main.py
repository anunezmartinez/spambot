import pyautogui, time, sys, keyboard

time.sleep(5)
for x in range(0, 100):
    if keyboard.is_pressed('q'):
        sys.exit()
    pyautogui.typewrite("juan")
    pyautogui.press("enter")
