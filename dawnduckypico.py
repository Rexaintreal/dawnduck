# This is the PICODUCKY EDITION 
# RUNS ON RASPBERRY PI PICO 
# USING Circuit python and usb HID to control the host computer
# NOT TESTED YET!!!!


import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# configurable settings like OS WEBSITES and Time Delay

# manually change the hardcoded OS here
OS="windows" # Can be "windows", "mac", "linux"

# hardcoded websites to open
WEBSITES = [
    "mail.google.com",
    "github.com",
    "leetcode.com",
    "instagram.com",
    "twitter.com",
    "linkedin.com",
    "keybr.com",
    "duolingo.com"
]

# time delay (change it if it is too fast or too slow)
TYPING_DELAY = 0.03

# Initialize keyboard
keyb = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyb)

# helping functions
def type_line(text, delay=None):
    """Type a line then press Enter"""
    if delay is None:
        delay = TYPING_DELAY
    
    for char in text:
        layout.write(char)
        time.sleep(delay)

    keyb.send(Keycode.ENTER)
    time.sleep(0.3)

def press_multi(*keys):
    """Pressing multiple keys (Shortcuts)"""
    keyb.press(*keys)
    time.sleep(0.05)
    keyb.release_all()  
    time.sleep(0.5)

def open_notesapp():
    """Open text editor based on hardcoded OS"""
    if OS == "windows":
        # Open Run dialog (Win+R)
        press_multi(Keycode.GUI, Keycode.R)
        time.sleep(0.5)
        
        # Type 'notepad' and press Enter
        layout.write("notepad")
        keyb.send(Keycode.ENTER)
        time.sleep(2)
        
        # Maximize window (Win+Up Arrow)
        press_multi(Keycode.GUI, Keycode.UP_ARROW)
        time.sleep(1)
        
    elif OS == "mac":
        # Open Spotlight (Cmd+Space)
        press_multi(Keycode.COMMAND, Keycode.SPACEBAR)
        time.sleep(0.5)
        
        # Type 'textedit' and press Enter
        layout.write("textedit")
        keyb.send(Keycode.ENTER)
        time.sleep(2)
        
        # Make fullscreen (Cmd+Ctrl+F)
        press_multi(Keycode.COMMAND, Keycode.CONTROL, Keycode.F)
        time.sleep(1)
        
    else:  # Linux
        # Open terminal (Ctrl+Alt+T)
        press_multi(Keycode.CONTROL, Keycode.ALT, Keycode.T)
        time.sleep(1)
        
        # Try to open gedit
        layout.write("gedit")
        keyb.send(Keycode.ENTER)
        time.sleep(2)



def switch_window():
    """Switch windows using alt tab or cmd tab"""
    if OS == "mac":
        press_multi(Keycode.COMMAND, Keycode.TAB)
    else:
        press_multi(Keycode.ALT, Keycode.TAB)
    time.sleep(0.5)

def open_browser_tab(): #idk how to open browsers directly so weve to keep it open ig T_T 
    """Open new browser tab using ctrl T"""
    if OS == "mac":
        press_multi(Keycode.COMMAND, Keycode.T)
    else:
        press_multi(Keycode.CONTROL, Keycode.T)
    time.sleep(0.8)

def open_website(url):
    """Open a website by typing its URL and pressing Enter"""
    open_browser_tab()

    layout.write(f"https://{url}")
    keyb.send(Keycode.ENTER)
    time.sleep(2)

def close_notes():
    """Close default notes app without saving"""
    if OS == "windows":
        press_multi(Keycode.CONTROL, Keycode.W)
        time.sleep(0.5)

        keyb.send(Keycode.TAB)
        time.sleep(0.5)

        keyb.send(Keycode.ENTER)

    elif OS == "mac":
        press_multi(Keycode.COMMAND, Keycode.Q)
        time.sleep(0.5)

        press_multi(Keycode.COMMAND, Keycode.D)
    else:  
        press_multi(Keycode.ALT, Keycode.F4)
        time.sleep(0.5)

        keyb.send(Keycode.TAB)
        time.sleep(0.5)

        keyb.send(Keycode.ENTER)


# main routine

def display_header():
    """Display cute header with spacing"""
    # Add spacing for better visibility
    for _ in range(8):
        keyb.send(Keycode.ENTER)
    
    # Display header
    type_line("$ DawnDuck - PicoDucky Edition")
    type_line("")
    type_line("[INFO] Loading morning routine...")
    type_line("")
    type_line("(^._.^)ﾉ  < Good meowrning!")
    type_line("")
    time.sleep(0.5)

def display_status_message():
    """Display status message (replaces time checking no real wake time checking on Pico)"""
    type_line("[INFO] Time to start your day!")
    type_line("[STATUS] PURRFECT TIMING LETS START THE DAY WOOHOOO")
    type_line("")
    time.sleep(1)

def open_all_websites():
    """Open all configured websites one by one"""
    type_line("[INFO] Opening websites...")
    type_line("")
    time.sleep(1)
    
    total = len(WEBSITES)
    
    for i, website in enumerate(WEBSITES, 1):
        # Display progress in notepad
        type_line(f"[{i}/{total}] Opening {website}...")
        
        # Switch to browser
        switch_window()
        time.sleep(0.5)
        
        # Open URL
        open_website(website)
        
        # Switch back to notepad
        switch_window()
        time.sleep(0.5)
    
    type_line("")
    type_line("[SUCCESS] All websites opened!")
    type_line("")
    time.sleep(1)

def display_goodbye():
    """Display goodbye message"""
    type_line("")
    type_line("(｡◕‿◕｡)  Have a great day!")
    type_line("")
    type_line("$ DawnDuck signing off...")
    type_line("$ ")
    time.sleep(2)

def run_morning_routine():
    """Main function that executes the complete morning routine using all the helper functions"""
    
    # Wait for USB to be fully recognized by system
    time.sleep(3)
    # Step 1: Open notepad/text editor
    open_notesapp()
    # Step 2: Display header and good morning message
    display_header()
    # Step 3: Display status (no time checking on Pico T_T)
    display_status_message()
    # Step 4: Open all websites
    open_all_websites()
    # Step 5: Display goodbye message
    display_goodbye()
    # Step 6: Close notepad
    close_notes()


# this runs automatically when PicoDucky is plugged in
run_morning_routine()