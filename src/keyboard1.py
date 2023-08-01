from pynput.keyboard import Key, Listener

x = 0

def on_press(key):
    if key == Key.up:
        global x
        x = x + 10
    print(f'{key} pressed')


def on_release(key):
    print(f'{key} release {x}')

    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
