# Acer RGB GUI for facer.py
## A GUI to interact with the acer-predator-turbo-and-rgb-keyboard-linux-module Acer Predator RGB kernel module from JafarAkhondali

### The keyboard lights in action
![](https://raw.githubusercontent.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/main/keyboard.webp)

### A look at the front-end application
![](https://raw.githubusercontent.com/ample-samples/web-portfolio/190384147cc67410606e54d72615f6b22b3a66ed/src/files/pictures/RGB%20Acer%20GUI.png)

This application was created to help users control their keyboard lights in a user-friendly way. This is a Linux only application designed for users of Arch Linux. This was created to solve the problem there being no programs to control acer keyboards on Linux.

## Installation

### Dependencies
The GUI requires Linux Headers, Python, Tkinter and CustomTkinter to run.

#### Arch
IMPORTANT NOTE: the linux headers are kernel specific. For example if you are using the zen-kernel, you would use ```linux-zen-headers``` instead of ```linux-headers```.
```
sudo pacman -S linux-headers python tk
yay -S customtkinter
```

### Install
```
git clone https://github.com/DJPretzel-bit64/acer-predator-rgb-gui --recursive
cd acer-predator-rgb-gui/acer-predator-turbo-and-rgb-keyboard-linux-module
chmod +x ./*.sh
sudo ./install_service.sh
```

### Run
To run the tool, simply run the python file "control.py" in the base directory.
```
cd /path/to/cloned/repo # cd ../.. if running directly after installation
./control.py
```

## Backend
The backend for this application can be found here: https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
