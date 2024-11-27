from pynput import keyboard

# Define the action to take when a key is pressed
def on_press(key):
    try:
        # Print the key code (scancode) for the ESC key when pressed
        if key == keyboard.Key.esc:
            print(f"ESC key pressed! Scancode: {key}")
            return False  # Exit listener after pressing ESC
    except AttributeError:
        pass

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Keep the listener running