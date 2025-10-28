<div align="center">

# DawnDuck

**Your friendly morning assistant that helps you start your day right**  
DawnDuck is a USB HID automation tool that opens your morning routine apps and websites automatically. It types cute messages and gets your day started.

[![Python 3.12.10](https://img.shields.io/badge/python-3.12.10-blue.svg)](https://www.python.org/downloads/release/python-31210/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-dawnduck-black?logo=github)](https://github.com/Rexaintreal/dawnduck)
[![Built for PicoDucky](https://img.shields.io/badge/Built%20for-PicoDucky-orange)](https://picoducky.hackclub.com/)
[![Hack Club Time](https://hackatime-badge.hackclub.com/U09B8FXUS78/dawnduck)](https://hackatime-badge.hackclub.com/U09B8FXUS78/dawnduck)

</div>

---

## Demo Video


**Thank you [Nico](https://github.com/RetrogradeDev) for testing it on Pico!**
Demo Video Using Pico (dawnduckpico.py) [WATCH IT HERE](https://drive.google.com/file/d/1jFVerF5OoLDsEQiagDVSvXAKIVcPKHfa/view?usp=sharing)



**FOR THE NON PICO ONE** [Watch it here](https://drive.google.com/file/d/1RgnQ6OoujTX302CRC5P6SvnvvXkUl29m/view?usp=sharing)

---

## Two Versions Available


### v1.0 - Desktop Python (For Testing)

The original version that runs on your computer. Good for testing and development without hardware.

**Features:**

- Cute good morning message with cat ASCII art

- Wake time checker - tells you if youre early or late

- Auto website opener - opens all your sites one by one

- Internet detection - checks connection before opening sites

- Cross-platform - Windows, macOS, Linux

- Customizable - JSON config for websites and wake time

- Terminal-style UI in Notepad

### v2.0 - PicoDucky Edition (Actual Hardware)

Rewritten for actual PicoDucky/Raspberry Pi Pico hardware using CircuitPython. Runs on the Pico itself and acts as a real USB keyboard.

**What changed:**

- Uses USB HID instead of desktop libraries

- Removed wake time checking - Pico has no RTC

- Removed internet detection - Pico cant check host connection

- Hardcoded config instead of JSON file

- Plug and play - no software needed on host computer

**What still works:**

- Opens notepad/text editor

- Types the same cute messages

- Opens all your websites

- Switches between windows

- Cross-platform support

---

## Getting Started

### Desktop Version (v1.0)

**Prerequisites:**

- Python 3.8+ (tested on 3.12.10)

- Admin/sudo permissions might be needed

**Installation:**

```bash

git clone https://github.com/Rexaintreal/dawnduck.git

cd dawnduck

pip install -r requirements.txt

```

**Configuration:**

Edit `config.json`:

```json

{

  "wake_up_time": "09:00",

  "websites": [

    "https://mail.google.com",

    "https://github.com",

    "https://leetcode.com"

  ]

}

```

**Usage:**

```bash

python dawnduck.py

```

Dont touch keyboard/mouse while its running. Takes about 30-60 seconds.

---

### PicoDucky Version (v2.0)


**Prerequisites:**

- PicoDucky or Raspberry Pi Pico board

- CircuitPython installed

- adafruit_hid library

**Installation:** 

**IM NOT SURE ABOUT THIS BASED ON MY RESEARCH FEEL FREE TO CHANGE IT OR CONTACT ME**

1. Install CircuitPython on your Pico:

  - Download from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico/)

  - Hold BOOTSEL while plugging in

  - Drag the .uf2 file to RPI-RP2 drive

  - Pico restarts as CIRCUITPY

2. Install adafruit_hid:

  - Download [CircuitPython Library Bundle](https://circuitpython.org/libraries)

  - Copy `adafruit_hid` folder to `lib` folder on CIRCUITPY

  - Should look like: `CIRCUITPY/lib/adafruit_hid/`

3. Upload code:

  - Copy `dawnduckpico.py` to CIRCUITPY root

  - Pico auto-restarts

**Configuration:**
Edit top of `dawnduckpico.py`:
```python

OS = "windows" # Change to "mac" or "linux" it might work for them too

WEBSITES = [

  "mail.google.com",

  "github.com",

  # add more here or remove it

]

TYPING_DELAY = 0.03 # adjust if too fast or too slow

```

**Usage:**
Please make sure only the browser is opened while plugging it in! 
1. Have a browser already open

2. Plug in PicoDucky

3. Dont touch anything for 60 seconds

4. Watch it work

---

## How It Works

**Desktop Version:**

1. Opens notepad using OS libraries
2. Types good morning message
3. Checks your wake time against current time
4. Tests internet connection
5. Opens each website using webbrowser module
6. Closes notepad

**PicoDucky Version:**

1. Waits 3 seconds for USB recognition
2. Opens notepad by sending Win+R then typing "notepad"
3. Types good morning message
4. Switches to browser with Alt+Tab (Browser needs to be opened before plugging in)
5. Opens new tabs with Ctrl+T and types URLs
6. Switches back to notepad after each site
7. Closes notepad


---


## File Structure

```
dawnduck/
├── dawnduck.py     # v1.0 Desktop version
├── dawnduckpico.py   # v2.0 PicoDucky version
├── config.json     # v1.0 configuration
├── requirements.txt   # v1.0 dependencies
└── README.md      # This file

```



---



## Troubleshooting

**Desktop Version:**

- Script doesnt type: Dont touch keyboard during execution
- Alt+Tab fails: Close other apps, increase delays
- Websites dont open: Check internet and URLs in config.json
- Permission errors: Run as admin/sudo



**PicoDucky Version:**

- Pico not recognized: Check CircuitPython is installed correctly
- Text in wrong place: Increase initial wait time to 5 seconds
- Websites dont open: Make sure browser is already running (yeah we need to open the browser manually)
- Wrong shortcuts: Change OS variable to match your system
- adafruit_hid not found: Make sure lib/adafruit_hid folder exists (im not sure as ive not tested yet on a pico)


Contact me if youre stuck.


---



## Technical Details



**v1.0 Dependencies:**

- keyboard (0.13.5) - Keyboard simulation
- pyautogui (0.9.54) - GUI automation
- distro (1.9.0) - Linux detection


**v2.0 Dependencies:**

- usb_hid - USB HID protocol (built-in)
- adafruit_hid - Keyboard control for CircuitPython

---



## PicoDucky Requirements Met

**Core:**

- Open source - full code available
- Demo video - linked above
- Detailed README - youre reading it
- Non-malicious - just helpful automation



**Extras:**

- Works offline - all code runs locally
- Cross-platform - Windows, Mac, Linux
- Multiple HID interfaces - keyboard automation
- Contained in board - v2.0 runs entirely on Pico *(NOT TESTED YET)*

---



## Contributing

Pull requests welcome. Add features, fix bugs, improve docs, or share your configs.


---



## License


MIT [LICENSE](LICENSE)



---



## Acknowledgements


[NICO For testing it!](https://github.com/RetrogradeDev) [his portfolio](https://pod.stio.studio/)
[REFERENCE DOCS](https://docs.circuitpython.org/projects/hid/en/latest/api.html)
[ADAFRUIT](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)
Built with help from tutorials and docs across the internet. Thanks to Hack Club for PicoDucky YSWS.



---



## More Projects



Check out my other stuff:

- [Libro Voice](https://github.com/Rexaintreal/Libro-Voice) - PDF to Audio Converter
- [Snippet Vision](https://github.com/Rexaintreal/Snippet-Vision) - YouTube Video Summarizer
- [Weather App](https://github.com/Rexaintreal/WeatherApp) - Python Weather Forecast App
- [Python Screenrecorder](https://github.com/Rexaintreal/PythonScreenrecorder) - Python Screen Recorder
- [Typing Speed Tester](https://github.com/Rexaintreal/TypingSpeedTester) - Python Typing Speed Tester
- [Movie Recommender](https://github.com/Rexaintreal/Movie-Recommender) - Python Movie Recommender
- [Password Generator](https://github.com/Rexaintreal/Password-Generator) - Python Password Generator
- [Object Tales](https://github.com/Rexaintreal/Object-Tales) - Python Image to Story Generator
- [Finance Manager](https://github.com/Rexaintreal/Finance-Manager) - Flask WebApp to Monitor Savings
- [Codegram](https://github.com/Rexaintreal/Codegram) - Social Media for Coders
- [Simple Flask Notes](https://github.com/Rexaintreal/Simple-Flask-Notes) - Flask Notes App
- [Key5](https://github.com/Rexaintreal/key5) - Python Keylogger
- [Codegram2024](https://github.com/Rexaintreal/Codegram2024) - Modern Codegram Update
- [Cupid](https://github.com/Rexaintreal/cupid) - Dating Web App for Teenagers
- [Gym Vogue](https://github.com/Rexaintreal/GymVogue/) - Ecommerce for Gym Freaks
- [Confessions](https://github.com/Rexaintreal/Confessions) - Anonymous Confession Platform
- [Syna](https://github.com/Rexaintreal/syna) - Social Music App with Spotify
- [Apollo](https://github.com/Rexaintreal/Apollo) - Minimal Music Player with Dancing Cat
- [Eros](https://github.com/Rexaintreal/Eros) - Face Symmetry Analyzer
- [Notez](https://github.com/Rexaintreal/Notez) - Clean Android Notes App
- [Lynx](https://github.com/Rexaintreal/lynx) - OpenCV Image Manipulation WebApp

---

## Author
Built by **Saurabh Tiwari**

- Email: [saurabhtiwari7986@gmail.com](mailto:saurabhtiwari7986@gmail.com)  
- Twitter: [@Saurabhcodes01](https://x.com/Saurabhcodes01)
- Instagram: [@saurabhcodesawfully](https://instagram.com/saurabhcodesawfully)
  
