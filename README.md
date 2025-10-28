<div align="center">

# DawnDuck v1.0

**Your friendly morning assistant that helps you start your day right!**  
DawnDuck is a USB HID automation tool that opens your morning routine apps and websites automatically.  
It types cute messages, checks if you're on time, and gets your day started!

[![Python 3.12.10](https://img.shields.io/badge/python-3.12.10-blue.svg)](https://www.python.org/downloads/release/python-31210/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-dawnduck-black?logo=github)](https://github.com/Rexaintreal/dawnduck)
[![Built for PicoDucky](https://img.shields.io/badge/Built%20for-PicoDucky-orange)](https://picoducky.hackclub.com/)
[![Hack Club Time](https://hackatime-badge.hackclub.com/U09B8FXUS78/dawnduck)](https://hackatime-badge.hackclub.com/U09B8FXUS78/dawnduck)

</div>


## Demo Video

[LINK](https://drive.google.com/file/d/1RgnQ6OoujTX302CRC5P6SvnvvXkUl29m/view?usp=sharing)

## Features

- **Cute Good Morning Message** - Starts your day with a friendly greeting  (cute cat hehe)
- **Wake Time Checker** - Tells you if you're early, on time, or oversleeping  (Based on the current time and specified wake time)
- **Auto Website Opener** - Opens all your important websites one by one  
- **Internet Detection** - Checks connection before opening sites  (pinging google DNS)
- **Cross-Platform** - Works on Windows, macOS, and Linux  (NOT TESTED ON LINUX AND MAC)
- **Customizable** - Easy JSON config for your websites and wake time  (just change the links and time more on this below)
- **Terminal-Style UI** - All actions displayed in Notepad with animations (Terminal like typing)

## Getting Started

### Prerequisites

- Python **3.8+** (tested on **3.12.10**)
- Admin/sudo permissions (required for keyboard automation im not really sure about this)

### Installation

1. Clone or download this repository:
```bash
git clone https://github.com/Rexaintreal/dawnduck.git
cd dawnduck
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

Edit `config.json` to customize your experience:

```json
{
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
```

- **wake_up_time**: Set your target wake-up time in 24-hour format (HH:MM)
- **websites**: Add or remove websites you want to open each morning 

## Usage

### Running the Script

**Option 1: Command Line**
```bash
python dawnduck.py
```

**Option 2: PowerShell (Windows)**
```powershell
& "C:/path/to/python.exe" "C:/path/to/dawnduck.py"
```

**Option 3: Right-click**
- Right-click `dawnduck.py`
- Select "Open with" → "Python"

### Important Notes

- Don’t use your keyboard or mouse while the script is running.
- It controls input for 30–60 seconds.
- Run with Admin/sudo privileges for full automation.

## How It Works

1. Opens your system’s text editor (like Notepad).
2. Displays a “Good Morning” message.
3. Checks your wake-up time and gives contextual feedback.
4. Tests your internet connection.
5. Opens each configured website sequentially.
6. Displays a goodbye message and closes Notepad.

## PicoDucky Requirements Met

### Core Requirements 
- **Open Source** - Full source code available
- **Demo Video** - [Link](https://drive.google.com/file/d/1RgnQ6OoujTX302CRC5P6SvnvvXkUl29m/view?usp=drive_link)
- **Detailed README** - You're reading it rn lol!
- **Non-Malicious** - Just helpful morning automation (I'll actually use it for leetcode day streaks and typing test)

### Extras
- **Works Offline** - All code runs locally (websites need internet tho)
- **Cross-Platform** - Windows, macOS, and Linux support
- **Multiple HID Interfaces** - Uses keyboard automation extensively
- **Contained in Board** - Currently Python script, can be ported to PicoDucky (I dont own a Pico RN T_T)

## Technical Details

### Dependencies
- `keyboard` (0.13.5) - Keyboard input simulation
- `pyautogui` (0.9.54) - GUI automation and hotkeys
- `distro` (1.9.0) - Linux distribution detection

### File Structure
```
dawnduck/
├── dawnduck.py          # Main script
├── config.json          # User configuration 
├── requirements.txt     # Python dependencies (install it to avoid any errors)
└── README.md           # This file
```

## Troubleshooting

**Script doesn't type in notepad**
- Make sure you're not touching keyboard/mouse during execution
- Check if notepad is properly focused after opening

**Alt+Tab doesn't return to notepad**
- Increase sleep delays in `focus_notepad()` function
- Close other applications before running

**Websites don't open**
- Check internet connection
- Verify URLs in `config.json` are correct

**PowerShell ampersand error**
- Wrap paths in quotes: `& "path/to/python.exe" "path/to/script.py"`

**Permission errors**
- Run terminal/PowerShell as Administrator (Windows)
- Use `sudo` on Linux/macOS

**Or just contact me!**

## Contributing

Pull requests welcome! Feel free to:
- Add new features
- Fix bugs
- Improve documentation
- Share your custom configs

## License

MIT [LICENSE](LICENSE).

---

## Acknowledgements

**THE INTERNET** - followed many tutorials, articles and webpages while building this.

---

## You may also like...

Some other projects I've built:

- [Libro Voice](https://github.com/Rexaintreal/Libro-Voice) - A PDF to Audio Converter
- [Snippet Vision](https://github.com/Rexaintreal/Snippet-Vision) - A YouTube Video Summarizer
- [Weather App](https://github.com/Rexaintreal/WeatherApp) - A Python Weather Forecast App
- [Python Screenrecorder](https://github.com/Rexaintreal/PythonScreenrecorder) - A Python Screen Recorder
- [Typing Speed Tester](https://github.com/Rexaintreal/TypingSpeedTester) - A Python Typing Speed Tester
- [Movie Recommender](https://github.com/Rexaintreal/Movie-Recommender) - A Python Movie Recommender
- [Password Generator](https://github.com/Rexaintreal/Password-Generator) - A Python Password Generator
- [Object Tales](https://github.com/Rexaintreal/Object-Tales) - A Python Image to Story Generator
- [Finance Manager](https://github.com/Rexaintreal/Finance-Manager) - A Flask WebApp to Monitor Savings
- [Codegram](https://github.com/Rexaintreal/Codegram) - A Social Media Web App for Coders
- [Simple Flask Notes](https://github.com/Rexaintreal/Simple-Flask-Notes) - A Flask Notes App
- [Key5](https://github.com/Rexaintreal/key5) - Python Keylogger
- [Codegram2024](https://github.com/Rexaintreal/Codegram2024) - A Modern Version of Codegram (Update)
- [Cupid](https://github.com/Rexaintreal/cupid) - A Dating Web App for Teenagers
- [Gym Vogue](https://github.com/Rexaintreal/GymVogue/) - Ecommerce Site for Gym Freaks
- [Confessions](https://github.com/Rexaintreal/Confessions) - Anonymous confession platform
- [Syna](https://github.com/Rexaintreal/syna) - A social music web application where users can log in using their Spotify accounts and find their best matches based on shared music preferences
- [Apollo](https://github.com/Rexaintreal/Apollo) - A Minimal Music Player with a Cat Dancing/Bopping to the beats
- [Eros](https://github.com/Rexaintreal/Eros) - A face symmetry analyzer built using Python and OpenCV
- [Notez](https://github.com/Rexaintreal/Notez) - A clean and minimal Android notes application built with Flutter
- [Lynx](https://github.com/Rexaintreal/lynx) - All in one OpenCV image manipulation webapp Built for [Hackberry](https://hackberry.hackclub.com/)
---

## Author

Built by **Saurabh Tiwari**

- Email: [saurabhtiwari7986@gmail.com](mailto:saurabhtiwari7986@gmail.com)  
- Twitter: [@Saurabhcodes01](https://x.com/Saurabhcodes01)
- Instagram: [@saurabhcodesawfully](https://instagram.com/saurabhcodesawfully)
