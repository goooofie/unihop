from time import sleep
import keyboard as kb

status = True

def change_status():
    global status
    status = not status
    print("Bunny Hop Activated" if status else "Bunny Hop Deactivated")

def bhop():
    global status
    while True:
        sleep(0.02)  # Adjust this interval based on your game's timing
        if status and kb.is_pressed("space"):
            kb.press_and_release("space")

if __name__ == "__main__":
    kb.add_hotkey("f1", change_status)
    print("Press 'f1' to toggle bunny hop script.")
    bhop()
