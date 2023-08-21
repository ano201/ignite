# Import necessary modules
from tkinter import *
import sentUnlimitedMessage  # Importing your custom module for handling messages
import webbrowser

# Create the main window
window = Tk()
title = window.title("Legendary Battle")
window.geometry("500x500")
window.attributes('-topmost', True)

# Initialize weapon mode and value
weaponMode = "select"
value = 0

# Create a menu bar
menubar = Menu(window)
window.config(menu=menubar)

# Create an "Exit" submenu under the menu bar
exit_menu = Menu(menubar)
menubar.add_cascade(label="Exit", command=window.destroy)

# Initialize menu flags
battle_menu_created = False
weapon_menu_created = False
ammo_menu_created = False


# Define a function to open a URL in a new browser tab
def callback(url):
    webbrowser.open_new_tab(url)


# Define a function that sets up the battle selection dropdown menu
def battle():
    # Create a StringVar to hold the selected battle field
    battle = StringVar()
    battle.set("Select Battle Field")

    # Create an OptionMenu (dropdown) widget with battle options and attach a command
    drop = OptionMenu(window, battle, "WhatsApp",
                      "Others", command=selected_battle)
    drop.grid(row=0, column=0, padx=10, pady=2, sticky="w")


# Create a label to display a clickable link
link = Label(window, text="", font=(
    'Helvetica', 15), fg="blue", cursor="hand2")
link.grid(row=1, column=0, padx=10, pady=2, sticky="w")


# Define a function to handle the selection of a battle field
def selected_battle(selected_battle_field):
    if selected_battle_field == "WhatsApp":
        # Update the label with a clickable link and bind it to the callback function
        link.config(text="Emoji Code Link", font=(
            'Helvetica', 15), fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e: callback(
            "https://khanmuhammadhridoy.github.io/whatsapp-web-emoji-keywords/"))
        link.grid(row=1, column=0, padx=10, pady=2, sticky="w")
    else:
        # Hide the label if a different battle field is selected
        link.grid_forget()

    # Create the weapon selection menu if it hasn't been created yet
    global battle_menu_created
    if not battle_menu_created:
        select_weapon()
        battle_menu_created = True


# Function to create and display the weapon selection menu
def select_weapon():
    message = StringVar()
    message.set("Select weapon")

    # Creating the OptionMenu widget for weapon selection
    messageOpt = OptionMenu(window, message, "Custom", "Random Word",
                            "Random character", "Random Special Character", command=selected_weapon)
    messageOpt.grid(row=2, column=0, padx=10, pady=2, sticky="w")


# Function to handle weapon selection
def selected_weapon(selected_weapon_name):
    global weaponMode

    # Handle custom weapon selection
    if selected_weapon_name == "Custom":
        weaponMode = "custom"
        # If customText widget doesn't exist, create and display it; otherwise, just show it
        if not hasattr(window, 'customText'):
            window.customText = custom_text()
        else:
            window.customText.grid(
                row=3, column=0, padx=10, pady=2, sticky="w")
    else:
        # If customText widget exists, hide it
        if hasattr(window, 'customText'):
            window.customText.grid_forget()

    # Set the weapon mode based on the selected option
    if selected_weapon_name == "Random Word":
        weaponMode = "randomword"
    elif selected_weapon_name == "Random character":
        weaponMode = "randomcharacter"
    elif selected_weapon_name == "Random Special Character":
        weaponMode = "randomspecialcharacter"

    # Create ammo selection menu if not already created
    global weapon_menu_created
    if not weapon_menu_created:
        select_ammo()
        weapon_menu_created = True


# Default message variable
message = " "


# Function to create and return the customText Entry widget
def custom_text():
    def a(event):
        global message
        message = customText.get()

    customText = Entry(window)
    customText.bind("<KeyRelease>", a)
    customText.grid(row=3, column=0, padx=10, pady=2, sticky="w")
    return customText


# Define the custom_text function that creates a text entry and binds a function to it
def custom_text():
    def a(event):
        global message
        message = customText.get()
    customText = Entry(window)
    customText.bind("<KeyRelease>", a)
    customText.grid(row=3, column=0, padx=10, pady=2, sticky="w")
    return customText


# Define the select_ammo function that creates an option menu for selecting ammunition type
def select_ammo():
    ammo = StringVar()
    ammo.set("Select Ammo")
    isCountable = OptionMenu(window, ammo, "Limited",
                             "Infinite", command=selected_ammo)
    isCountable.grid(row=4, column=0, padx=10, pady=2, sticky="w")


# Function to handle changes in selected ammunition
def selected_ammo(selected_ammunition):
    global value

    # Check if selected ammunition is "Limited"
    if selected_ammunition == "Limited":
        if not hasattr(window, 'message'):
            window.message = message_limit()  # Create a message count entry
        else:
            # Show the existing message count entry
            window.message.grid(row=5, column=0, padx=10, pady=2, sticky="w")
    else:
        if hasattr(window, 'message'):
            window.message.grid_forget()  # Hide the message count entry

    # Reset value if ammunition is "Infinite"
    if selected_ammunition == "Infinite":
        value = 0

    # Create an ammo menu if not already created
    global ammo_menu_created
    if not ammo_menu_created:
        ignite()  # Create the "Ignite" button
        ammo_menu_created = True


# Function to create the message count entry
def message_limit():
    def a(event):
        global value
        value = message_count.get()
    message_count = Entry(window)
    message_count.bind("<KeyRelease>", a)
    message_count.grid(row=5, column=0, padx=10, pady=2, sticky="w")
    return message_count


# Function to create the "Ignite" button
def ignite():
    button = Button(window, text="Ignite", command=lambda: sentUnlimitedMessage.sentUnlimitedMessages(
        weaponMode, message, int(value)))
    button.grid(row=6, column=0, padx=10, pady=2, sticky="w")


# This line seems to call a function named 'battle', which might be responsible for handling game mechanics or logic.
battle()

# This line seems to update the GUI window, reflecting any changes made during the 'battle' function.
window.update()

# This line appears to start the main event loop of the GUI application, which keeps the program running and responsive to user interactions.
window.mainloop()
