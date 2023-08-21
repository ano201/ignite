# pip install pyautogui

from tkinter import *  # Import the tkinter library for creating graphical user interfaces

import pyautogui  # Import the pyautogui module
import time  # Import the time module for adding a delay
from wonderwords import RandomWord  # Import random words

import secrets  # Import the secrets module for cryptographic operations
import random   # Import the random module for generating random values
import string   # Import the string module for working with strings


w = RandomWord()  # Create an instance of the RandomWord class for generating random words


def randomCharecter():
    # Generate a random string of characters including letters, digits, and punctuation
    special = ''.join((secrets.choice(string.ascii_letters +
                      string.digits + string.punctuation) for i in range(20)))
    return special


def randomSpeicalCharecter():
    # Generate a random string of punctuation characters
    c = ''.join((secrets.choice(string.punctuation) for i in range(20)))
    return c

    # return w.word(starts_with="a", ends_with="a")


def randomWord():
    # Generate and return a random word using the 'w' instance of RandomWord
    return w.word()

# time.sleep(3)  # Add a delay of seconds


# value = 1  # Set the value for how many message to send


# Loop for sending messages
# def send():

#     pyautogui.typewrite(":boo")
#     pyautogui.typewrite("\n")

    # pyautogui.typewrite("\n")

    # pyautogui.typewrite(" ")
    # for i in range(10):
    #     # for facebook messages
    #     pyautogui.typewrite(message())
    #     pyautogui.typewrite(" ")


def ammo(weaponMode, message):
    # Send a message based on the selected weapon mode.
    if weaponMode == "custom":
        # Send the custom message twice to simulate sending
        pyautogui.typewrite(message)
        pyautogui.typewrite("\n")
        pyautogui.typewrite("\n")
    elif weaponMode == "randomword":
        # Send a message composed of random words
        pyautogui.typewrite(
            f"{randomWord()} {randomWord()} {randomWord()} {randomWord()} {randomWord()} \n")
    elif weaponMode == "randomcharacter":
        # Send a message composed of random characters
        pyautogui.typewrite(f"{randomCharecter()}\n")
    elif weaponMode == "randomspecialcharacter":
        # Send a message composed of random special characters
        pyautogui.typewrite(f"{randomSpeicalCharecter()}\n")


def sentUnlimitedMessages(weaponMode, message, value):
    # Send a specified number of messages based on the selected weapon mode.
    time.sleep(5)
    if value == 0:
        # Send messages indefinitely
        while True:
            ammo(weaponMode, message)
    else:
        # Send a specified number of messages
        for i in range(value):
            ammo(weaponMode, message)
    # Press Enter after sending messages
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
