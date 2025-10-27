import time
import keyboard
import platform
import pyautogui

def open_notesapp():
    """Open the default notes app based on the operating system."""
    os_name = platform.system()
    
    if os_name == "Windows":
        keyboard.press_and_release('win + r')
        time.sleep(0.5)
        keyboard.write('notepad', delay=0.1)
        keyboard.press_and_release('enter')
        time.sleep(1.5)
        keyboard.press_and_release('win+up')  # Maximize window
        time.sleep(0.5)
        
    elif os_name == "Darwin":  # macOS
        keyboard.press_and_release('cmd+space')
        time.sleep(0.5)
        keyboard.write('textedit', delay=0.1)
        keyboard.press_and_release('enter')
        time.sleep(1.5)
        keyboard.press_and_release('cmd+ctrl+f')  # Full screen
    
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
    
    time.sleep(1)

def type_good_morning():
    """Types a cute good morning message like terminal output."""
    # nto sure about the alignement, adjust as needed
    # Add vertical spacing
    for _ in range(10):
        keyboard.press_and_release('enter')
    
    lines = [
        r"$ DawnDuck v1.0 initializing...",
        r"",
        r"[INFO] Loading morning routine...",
        r"",
        r"(^._.^)ﾉ  < Good meowrning!",
        r"",
        r"$ "
    ]
    
    for line in lines:
        keyboard.write(line, delay=0.02)
        keyboard.press_and_release('enter')
        time.sleep(0.05)

def close_notepad():
    """Closes Notepad/TextEdit without saving."""
    os_name = platform.system()
    
    time.sleep(2)
    
    if os_name == "Windows":
        # Close with Ctrl+W
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        # Click on the dont save button using Tab and Enter
        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('enter')
        
    elif os_name == "Darwin":
        # macOS - Cmd+W to close
        pyautogui.hotkey('cmd', 'w')
        time.sleep(0.5)
        pyautogui.hotkey('cmd', 'd')  # Don't Save shortcut
        
    else:  # Linux
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('enter')

def main():
    """Main function to call all the functions."""
    print("DawnDuck V1.0")
    print("Opening notepad")
    time.sleep(2)
    
    open_notesapp()
    type_good_morning()
    
    time.sleep(3)
    close_notepad()
    

if __name__ == "__main__":
    main()