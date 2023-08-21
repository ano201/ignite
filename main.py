from tkinter import *
import sentUnlimitedMessage
import webbrowser

window = Tk()
title = window.title("Legendary Battle")
window.geometry("500x500")
window.attributes('-topmost', True)

weaponMode = "select"
value = 0
menubar = Menu(window)
window.config(menu=menubar)

exit_menu = Menu(menubar)
menubar.add_cascade(label="Exit", command=window.destroy)

battle_menu_created = False
weapon_menu_created = False

ammo_menu_created = False


def callback(url):
    webbrowser.open_new_tab(url)


def battle():
    battle = StringVar()
    battle.set("Select Battle Field")
    drop = OptionMenu(window, battle, "WhatsApp",
                      "Others", command=selected_battle)
    drop.grid(row=0, column=0, padx=10, pady=2, sticky="w")


link = Label(window, text="", font=(
    'Helvetica', 15), fg="blue", cursor="hand2")
link.grid(row=1, column=0, padx=10, pady=2, sticky="w")


def selected_battle(selected_battle_field):
    if selected_battle_field == "WhatsApp":
        link.config(text="Emoji Code Link", font=(
            'Helvetica', 15), fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e: callback(
            "https://khanmuhammadhridoy.github.io/whatsapp-web-emoji-keywords/"))
        link.grid(row=1, column=0, padx=10, pady=2,
                  sticky="w")

    else:
        link.grid_forget()

    global battle_menu_created
    if not battle_menu_created:
        select_weapon()
        battle_menu_created = True


def select_weapon():
    message = StringVar()
    message.set("Select weapon")
    messageOpt = OptionMenu(window, message, "Custom", "Random Word",
                            "Random character", "Random Special Character", command=selected_weapon)
    messageOpt.grid(row=2, column=0, padx=10, pady=2, sticky="w")


def selected_weapon(selected_weapon_name):
    global weaponMode
    if selected_weapon_name == "Custom":
        weaponMode = "custom"
        if not hasattr(window, 'customText'):
            window.customText = custom_text()
        else:
            window.customText.grid(
                row=3, column=0, padx=10, pady=2, sticky="w")
    else:
        if hasattr(window, 'customText'):
            window.customText.grid_forget()
    if selected_weapon_name == "Random Word":
        weaponMode = "randomword"
    elif selected_weapon_name == "Random character":
        weaponMode = "randomcharacter"
    elif selected_weapon_name == "Random Special Character":
        weaponMode = "randomspecialcharacter"

    global weapon_menu_created
    if not weapon_menu_created:
        select_ammo()
        weapon_menu_created = True


message = " "


def custom_text():
    def a(event):
        global message
        message = customText.get()
    customText = Entry(window)
    customText.bind("<KeyRelease>", a)
    customText.grid(row=3, column=0, padx=10, pady=2, sticky="w")
    return customText


def select_ammo():
    ammo = StringVar()
    ammo.set("Select Ammo")
    isCountable = OptionMenu(window, ammo, "Limited",
                             "Infinite", command=selected_ammo)
    isCountable.grid(row=4, column=0, padx=10, pady=2, sticky="w")


def selected_ammo(selected_ammunition):
    global value
    if selected_ammunition == "Limited":
        if not hasattr(window, 'message'):
            window.message = message_limit()
        else:
            window.message.grid(row=5, column=0, padx=10, pady=2, sticky="w")
    else:
        if hasattr(window, 'message'):
            window.message.grid_forget()
    if selected_ammunition == "Infinite":
        value = 0

    global ammo_menu_created
    if not ammo_menu_created:
        ignite()
        ammo_menu_created = True


def message_limit():
    def a(event):
        global value
        value = message_count.get()
        # value.append(message_count.get())
    # , validate="key", validatecommand=(        window.register(validate_input), "%P")
    # def validate_input(P):
    #     return P.isdigit()
    message_count = Entry(window)
    message_count.bind("<KeyRelease>", a)
    message_count.grid(row=5, column=0, padx=10, pady=2, sticky="w")
    return message_count


def ignite():

    button = Button(window, text="Ignite",
                    command=lambda: sentUnlimitedMessage.sentUnlimitedMessages(weaponMode, message, int(value)))
    button.grid(row=6, column=0, padx=10, pady=2, sticky="w")


battle()
window.update()
window.mainloop()
