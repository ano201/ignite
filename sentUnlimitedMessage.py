# pip install pyautogui

from tkinter import *

import pyautogui  # Import the pyautogui module
import time  # Import the time module for adding a delay
from wonderwords import RandomWord  # Import random words

import secrets
import random
import string


w = RandomWord()


def randomCharecter():
    special = ''.join((secrets.choice(string.ascii_letters +
                      string.digits + string.punctuation) for i in range(20)))
    return (special)


def randomSpeicalCharecter():
    c = ''.join((secrets.choice(string.punctuation) for i in range(20)))
    return (c)

    # return w.word(starts_with="a", ends_with="a")


def randomWord():
    return w.word()


# time.sleep(3)  # Add a delay of seconds


# value = 1  # Set the value for how many message to send


# Loop for sending messages
def send():

    pyautogui.typewrite(":boo")
    pyautogui.typewrite("\n")

    # pyautogui.typewrite("\n")

    # pyautogui.typewrite(" ")
    # for i in range(10):
    #     # for facebook messages
    #     pyautogui.typewrite(message())
    #     pyautogui.typewrite(" ")


def ammo(weaponMode, message):
    if weaponMode == "custom":
        pyautogui.typewrite(message)
        pyautogui.typewrite("\n")
        pyautogui.typewrite("\n")
    elif weaponMode == "randomword":
        pyautogui.typewrite(
            f"{randomWord()} {randomWord()} {randomWord()} {randomWord()} {randomWord()} \n")
    elif weaponMode == "randomcharacter":
        pyautogui.typewrite(f"{randomCharecter()}\n")
    elif weaponMode == "randomspecialcharacter":
        pyautogui.typewrite(f"{randomSpeicalCharecter()}\n")


def sentUnlimitedMessages(weaponMode, message, value):
    time.sleep(5)
    if value == 0:
        while True:
            ammo(weaponMode, message)
    else:
        for i in range(value):
            ammo(weaponMode, message)
    pyautogui.press('enter')

    # time.sleep(3)
    # print("value", value)
    # for i in range(value):
    #     send()
    #     pyautogui.press('enter')

    # for whatsapp uncomment 2 lines below
    # pyautogui.typewrite(':boo')
    # pyautogui.press('enter')


# Loop to copy and paste text
# for i in range(3):
#     # Select all text
#     pyautogui.hotkey('ctrl', 'a')
#     # Copy selected text
#     pyautogui.hotkey('ctrl', 'c')
#     # Move to the next line
#     pyautogui.press('down')
#     # Paste the copied text
#     pyautogui.hotkey('ctrl', 'v')
#     # Select all text again
#     pyautogui.hotkey('ctrl', 'a')
#     # Copy selected text again
#     pyautogui.hotkey('ctrl', 'c')

# Loop to paste the copied text multiple times
# for i in range(value):
    # Paste the copied text
    # pyautogui.hotkey('ctrl', 'v')
    # Press Enter
    # pyautogui.press('enter')
