import time
import keyboard
import platform
import pyautogui
import socket
import webbrowser
import os
import json
from datetime import datetime

def open_notesapp():
    """Open the default notes app based on the operating system."""
    os_name = platform.system()
    
    if os_name == "Windows":
        keyboard.press_and_release('win + r')
        time.sleep(0.5)
        keyboard.write('notepad', delay=0.1)
        keyboard.press_and_release('enter')
        time.sleep(2)
        keyboard.press_and_release('win+up')  # Maximize window
        time.sleep(1)
        
    elif os_name == "Darwin":  # macOS
        keyboard.press_and_release('cmd+space')
        time.sleep(0.5)
        keyboard.write('textedit', delay=0.1)
        keyboard.press_and_release('enter')
        time.sleep(2)
        keyboard.press_and_release('cmd+ctrl+f')  # Full screen
        time.sleep(1)
    
    else:  # Linux
        try:
            import distro
            distro_name = distro.id().lower()
        except:
            distro_name = "unknown"
        
        keyboard.press_and_release('ctrl+alt+t')
        time.sleep(1)
        
        if 'ubuntu' in distro_name or 'debian' in distro_name:
            keyboard.write('gedit', delay=0.1)
        elif 'fedora' in distro_name or 'centos' in distro_name:
            keyboard.write('gedit', delay=0.1)
        elif 'arch' in distro_name:
            keyboard.write('gedit || nano', delay=0.1)
        else:
            keyboard.write('nano', delay=0.1)
        keyboard.press_and_release('enter')
        time.sleep(2)

def focus_notepad():
    """Bring notepad back to focus."""
    os_name = platform.system()
    
    if os_name == "Windows":
        # Alt+Tab to cycle back to notepad
        keyboard.press_and_release('alt+tab')
        time.sleep(0.5)
        
    elif os_name == "Darwin":
        # Cmd+Tab on macOS
        keyboard.press_and_release('cmd+tab')
        time.sleep(0.5)
        
    else:  # Linux
        keyboard.press_and_release('alt+tab')
        time.sleep(0.5)

def check_internet():
    """Check if internet connection is working."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def load_config():
    """Load websites from config.json or create default if it doesn't exist"""
    default_config = {
        "wake_up_time": "09:00",
        "websites": [
            "https://mail.google.com",
            "https://github.com",
            "https://leetcode.com",
            "https://instagram.com",
            "https://twitter.com",
            "https://linkedin.com",
            "https://keybr.com",
            "https://duolingo.com"
        ]
    }
    
    config_path = "config.json"
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=4)
        return default_config
    else:
        with open(config_path, 'r') as f:
            return json.load(f)

def type_message(text, delay=0.03):
    """Type every message with proper delay"""
    keyboard.write(text, delay=delay)
    keyboard.press_and_release('enter')
    time.sleep(0.3)

def type_good_morning():
    """Types a cute good morning message with a cat UwU"""
    # Add spacing
    for _ in range(8):
        keyboard.press_and_release('enter')
    
    type_message(r"$ DawnDuck v1.0 initializing...")
    type_message(r"")
    type_message(r"[INFO] Loading morning routine...")
    type_message(r"")
    type_message(r"(^._.^)ﾉ  < Good meowrning!")
    type_message(r"")
    time.sleep(0.5)

def check_wake_up_time(target_time):
    """Check if user woke up on time and return messages based on the current time"""
    try:
        # Parse target time (HH:MM)
        target_hour, target_minute = map(int, target_time.split(':'))

        # Get current time
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # Convert to minutes for easier comparison
        target_minutes = target_hour * 60 + target_minute
        current_minutes = current_hour * 60 + current_minute

        # Calculating the difference between now and the wake up time 
        diff = current_minutes - target_minutes

        # message based on the time diff
        if diff <= -30:
            return r"Woke Up too early did you get the right amount of sleep?"
        elif diff < 0:
            return r"a bit early eh? Niceeee!"
        elif diff < 15:
            return r"PURRFECT TIMING LETS START THE DAY WOOHOOO"
        elif diff <= 30:
            return r"Slept a bit too much? No worries we can catch up easily"
        elif diff <= 60:
            return r"Overslept? BE ON TIME TOMORROW!!"
        elif diff <= 120:
            return r"Where were you DAWG? YOU MISSED HALF THE MORNING!!"
        else:
            return r"Really? this late? are you feeling okay?? Anyways lets get started"

    except Exception as e:
        return "Couldn't check wake time, but good morning anyway!"

def display_wake_time_check(target_time):
    """Display wake time check in notepad."""
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    
    type_message(f"[INFO] Current time: {current_time}")
    type_message(f"[INFO] Target wake time: {target_time}")
    time.sleep(0.5)
    
    message = check_wake_up_time(target_time)
    type_message(f"[STATUS] {message}")
    type_message(r"")
    time.sleep(1)

def check_and_display_internet():
    """checking internet connection and displaying status."""
    type_message(r"[INFO] Checking internet connection...")
    time.sleep(1)
    
    if check_internet():
        type_message(r"[SUCCESS] Internet connection found! ✓")
        type_message(r"")
        return True
    else:
        type_message(r"[ERROR] No internet connection found ✗")
        type_message(r"")
        return False

def open_websites(websites):
    """Open websites one by one, returning to notepad after each."""
    type_message(r"[INFO] Opening websites...")
    type_message(r"")
    time.sleep(1)
    
    for i, website in enumerate(websites, 1):
        # Extract domain name for display
        domain = website.replace('https://', '').replace('http://', '').split('/')[0]
        type_message(f"[{i}/{len(websites)}] Opening {domain}...")
        
        # Open website
        webbrowser.open(website)
        time.sleep(2)  # Wait for browser to open
        
        # Return focus to notepad
        focus_notepad()
        time.sleep(0.5)
    
    type_message(r"")
    type_message(r"[SUCCESS] All websites opened!")
    type_message(r"")

def type_goodbye():
    """Type goodbye message."""
    time.sleep(1)
    type_message(r"")
    type_message(r"(｡◕‿◕｡)  Have a great day!")
    type_message(r"")
    type_message(r"$ DawnDuck signing off...")
    type_message(r"$ ")
    time.sleep(2)

def close_notepad():
    """Closes Notepad/TextEdit without saving."""
    os_name = platform.system()
    
    time.sleep(1)
    
    if os_name == "Windows":
        pyautogui.hotkey('ctrl', 'w')  # alt+f4 was not working for me maybe because of some focus issue or laptop fn button
        time.sleep(0.5) 
        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('enter')
        
    elif os_name == "Darwin":
        pyautogui.hotkey('cmd', 'q')
        time.sleep(0.5)
        pyautogui.hotkey('cmd', 'd')
        
    else:  # Linux
        pyautogui.hotkey('alt', 'f4')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('enter')

def main():
    """Main function to run DawnDuck"""
    print("=" * 50)
    print("DawnDuck V1.0")
    print("=" * 50)
    print("\nStarting...")
    
    # Load config
    config = load_config()
    
    # Open notepad
    print("\n[1/6] Opening notepad...")
    open_notesapp()
    
    # Type good morning
    print("[2/6] Typing good morning message...")
    type_good_morning()
    
    # Check wake time
    print("[3/6] Checking wake time...")
    display_wake_time_check(config.get('wake_up_time', '09:00'))
    
    # Check internet
    print("[4/6] Checking internet connection...")
    internet_available = check_and_display_internet()
    
    # Open websites if internet is available
    if internet_available:
        print("[5/6] Opening websites (switching back to notepad after each website)...")
        open_websites(config['websites'])
    else:
        print("[5/6] Skipping websites (no internet)...")
        time.sleep(2)
    
    # Type goodbye
    print("[6/6] Saying goodbye...")
    type_goodbye()
    
    # Close notepad
    print("\nClosing notepad...")
    close_notepad()
    
    print("\n" + "=" * 50)
    print("Completed successfully with no Errors!")
    print("=" * 50)

if __name__ == "__main__":
    main()