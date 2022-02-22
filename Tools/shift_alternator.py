from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode, Listener
import time

# Make a program that switches caps lock on and off every key press.
caps_lock = KeyCode(char="Caps Lock")
