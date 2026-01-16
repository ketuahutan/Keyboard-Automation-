import time
import keyboard

# Global toggle state
spamming = False

def toggle_spam():
    global spamming
    spamming = not spamming
    print(f"Spamming {'enabled' if spamming else 'disabled'}")

# Set up hotkey to toggle (press F12 to toggle)
keyboard.add_hotkey('f12', toggle_spam)

print("Press F12 to toggle z-spamming. Press ESC to exit.")

# Main loop
while True:
    if spamming:
        keyboard.press('z')
        time.sleep(0.05)
    time.sleep(0.01)  # Small delay to prevent high CPU usage

    # Check for exit key
    if keyboard.is_pressed('f12'):
        break