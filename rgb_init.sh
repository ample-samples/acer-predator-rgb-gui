#!/bin/bash

# Link to Github readme:
# https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module


mode=1
red=100
green=30
blue=235


acer-predator-turbo-and-rgb-keyboard-linux-module/facer_rgb.py -m "$mode" -z 1 -cR "$red" -cG "$green" -cB "$blue"
acer-predator-turbo-and-rgb-keyboard-linux-module/facer_rgb.py -m "$mode" -z 2 -cR "$red" -cG "$green" -cB "$blue"
acer-predator-turbo-and-rgb-keyboard-linux-module/facer_rgb.py -m "$mode" -z 3 -cR "$red" -cG "$green" -cB "$blue"
acer-predator-turbo-and-rgb-keyboard-linux-module/facer_rgb.py -m "$mode" -z 4 -cR "$red" -cG "$green" -cB "$blue"

