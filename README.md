# Acer RGB GUI for facer.py
## A GUI to interact with the acer-predator-turbo-and-rgb-keyboard-linux-module Acer Predator RGB kernel module from JafarAkhondali

### The keyboard lights in action
![](https://raw.githubusercontent.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/main/keyboard.webp)

### A look at my front-end application
![](https://raw.githubusercontent.com/ample-samples/web-portfolio/190384147cc67410606e54d72615f6b22b3a66ed/src/files/pictures/RGB%20Acer%20GUI.png)

This application was created to help users control their keyboard lights in a user-friendly way. This is a Linux only application designed for users of Arch Linux. I created this to solve the problem I had which was when I had just started using Linux and found that there were no programs to control my laptop's lights in an easy way.

## Installation

### Dependencies
The GUI requires Python, Tkinter and CustomTkinter to run.

#### Arch Installation
```
sudo pacman -S python tk
yay -S customtkinter
```

### Install
```
git clone https://github.com/ample-samples/acer-predator-rgb-gui
cd acer-predator-rgb-gui
git clone https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
cd acer-predator-turbo-and-rgb-keyboard-linux-module
chmod +x ./.sh
sudo ./install.sh
```

### Run
Open the "rgb Keyboard GUI" folder and run "RGB Control.py". To activate the custom profile, run 

## Backend
The backend for this application can be found here: https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
