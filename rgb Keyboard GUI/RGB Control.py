#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import subprocess
import customtkinter
import pickle
from math import *
from dataclasses import dataclass

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



@dataclass
class rgb_profile:
    mode: int = 0
    red: float = 0
    green: float = 0
    blue: float = 0

profile_1 = rgb_profile()
print(profile_1.mode)





class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("RGB Control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing) #call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="RGB Control",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="RGB7",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_7)
        self.button_1.grid(row=4, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="RGB3",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_3)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="RGB6",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_6)
        self.button_3.grid(row=2, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Autostart",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.set_autostart)
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="rAnDoM",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_9)

        self.button_5.grid(row=6, column=0, pady=10, padx=20)


        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(9, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(5, weight=1)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure((0, 4), weight=1)

        self.label_preview = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Preview" ,
                                                   text_font=('Roboto medium', -16),
                                                   height=100,
                                                   fg_color='#000000',  # <- custom tuple-color
                                                   justify=tkinter.LEFT,
                                                   bg_color='#000000')
                                                   
        self.label_preview.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)


        # ============ frame_right ============
        # SLIDER & LABEL RED
        self.slider_r = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=255,
                                                command=self.update_red)
        self.slider_r.grid(row=4, column=0, columnspan=1, pady=10, padx=20, sticky="we") 

        self.label_r = customtkinter.CTkLabel(master=self.frame_right,
                                              text=self.slider_r.get(),
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_r.grid(row=4, column=1, columnspan=1, pady=10, padx=0)


        # SLIDER & LABEL GREEN
        self.slider_g = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=255,
                                                command=self.update_green)
        self.slider_g.grid(row=5, column=0, columnspan=1, pady=10, padx=20, sticky="we")
        

        self.label_g = customtkinter.CTkLabel(master=self.frame_right,
                                              text=self.slider_g.get(),
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_g.grid(row=5, column=1, columnspan=1, pady=10, padx=0)

        # SLIDER & LABEL BLUE
        self.slider_b = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=255,
                                                command=self.update_blue)
        self.slider_b.grid(row=6, column=0, columnspan=1, pady=10, padx=20, sticky="we")
        

        self.label_b = customtkinter.CTkLabel(master=self.frame_right,
                                              text=self.slider_b.get(),
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_b.grid(row=6, column=1, columnspan=1, pady=10, padx=0)

        self.button_set_colour = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Set colour",
                                                       command=self.set_colour)
        self.button_set_colour.grid(row=7, column=1, columnspan=1, pady=10, padx=20, sticky="we")

        self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Load profile",
                                                       command=self.load_profile)
        self.slider_button_2.grid(row=7, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.set_autostart_button = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Set autostart",
                                                       command=self.set_colour)
        self.set_autostart_button.grid(row=8, column=1, columnspan=1, pady=10, padx=20, sticky="we")

        self.load_autostart_button = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Load autostart",
                                                       command=self.load_profile)
        self.load_autostart_button.grid(row=8, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Save as")
        self.entry.grid(row=10, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Save profile",
                                                command=self.save_profile)
        self.button_5.grid(row=10, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.mode = tkinter.IntVar(value=0)


        # RADIO BUTTONS, MODE SELECT
        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Mode select:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_0 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.mode,
                                                           value=0,
                                                           text='Static')
        self.radio_button_0.grid(row=1, column=2, pady=5, padx=20, sticky="n")


        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.mode,
                                                           value=1,
                                                           text='Breath')
        self.radio_button_1.grid(row=2, column=2, pady=5, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.mode,
                                                           value=2,
                                                           text='Neon' )
        self.radio_button_2.grid(row=3, column=2, pady=5, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.mode,
                                                           value=3,
                                                           text='Wave')
        self.radio_button_3.grid(row=4, column=2, pady=5, padx=20, sticky="n")



        # set default values
        self.radio_button_0.select()
        self.switch_2.select()
        self.slider_r.set(0)
        self.slider_g.set(0)
        self.slider_b.set(0)


    rgb_1 = rgb_profile(1, 255, 0, 0)
    print(rgb_1)
    profile_default = rgb_profile(0, 0, 255, 0)
    
    # SAVES THE CURRENT OPTIONS TO THE AUTOSTART PICKLE OBJECT AND THE bin/rgb_autostart.sh PROGRAM
    def set_autostart(self):
        template = """ 
        #!/bin/bash 
        echo {xi} 
        """
        print(template.format(xi = 'bants'))
        facer_path = '/home/todd/Programs/acer-predator-turbo-and-rgb-keyboard-linux-module/facer_rgb.py'
        return template

    # LOADS THE CURRENTLY SET AUTOSTART PICKLE OBJECT 
    def load_autostart(self):
        return None

    # SAVES THE CURRENT OPTIONS TO rgb_profile_<PROFILE NAME>
    def save_profile(self):

        profile_name = "/home/todd/Programs/Acer RGB/rgb_profile_" + self.entry.get()
        profile = rgb_profile(
            self.mode.get(),
            self.slider_r.get(),
            self.slider_g.get(),
            self.slider_b.get()
        )
        print(profile)
        with open(profile_name, "wb") as file:
            pickle.dump(profile, file)

    # LOADS THE GIVEN PROFILE FROM rgb_profile_<PROFILE NAME>
    def load_profile(self):
        profile_name = "/home/todd/Programs/Acer RGB/rgb_profile_" + self.entry.get()
        with open(profile_name, "rb") as file:
            profile_obj = pickle.load(file)
            self.mode.set(profile_obj.mode)
            self.slider_r.set(profile_obj.red)
            self.slider_g.set(profile_obj.green)
            self.slider_b.set(profile_obj.blue)
            print(profile_obj)
        self.update_preview()

    def button_event(self):
        print("Button pressed")

    def rgb_autostart(self):
        subprocess.run(["rgb_autostart"])

    def rgb_init_6(self):
        subprocess.run(["rgb_init.sh_6"])

    def rgb_init_7(self):
        subprocess.run(["rgb_init.sh_7"])

    def rgb_init_8(self):
        subprocess.run(["rgb_init.sh_9"])

    def rgb_init_9(self):
        subprocess.run(["rgb_init.sh_9"])

    def rgb_init_3(self):
        subprocess.run(["rgb_init.sh_3"])

    def rgb_init_2(self):
        subprocess.run(["rgb_init.sh_2"])

    def update_red(self, slider):
        red = slider
        self.label_r.config(text=str(int(red*255)))
        self.update_preview()
    
    def update_green(self, slider):
        green = slider
        self.label_g.config(text=str(int(green*255)))
        self.update_preview()

    def update_blue(self, slider):
        blue = slider
        self.label_b.config(text=str(int(blue*255)))
        self.update_preview()

    def return_red(self):
        red = int(self.slider_r.get() * 255)
        return red 

    def return_green(self):
        green = int(self.slider_g.get() * 255)
        return green 

    def return_blue(self):
        blue = int(self.slider_b.get() * 255)
        return blue 

    def update_preview(self):
        red = self.return_red()
        green = self.return_green()
        blue = self.return_blue()
        rgb_255 = (red, green, blue)
        rgb_hex = '#%02x%02x%02x' % rgb_255
        self.label_preview.configure(fg_color=rgb_hex)
        return rgb_hex

    # RETRIEVES THE VALUES OF THE MODE AND THE R G AND B SLIDERS AND EXECUTES A COMMAND TO SET IT
    def set_colour(self):
        mode = self.mode.get()
        red = int(self.slider_r.get() * 255 )
        green = int(self.slider_g.get() * 255 )
        blue = int(self.slider_b.get() * 255 )
        facer_path = '/home/todd/Programs/acer-predator-turbo-and-rgb-keyboard-linux-module/facer_rgb.py'
        for i in range(1, 5):
            zone = i
            print(facer_path +' -m {} -z {} -cR {} -cG {} -cB {}'.format(mode, zone, red, green, blue)
                 )
            subprocess.run(
                [facer_path,
                 '-m', '{}'.format(mode),
                 '-z', '{}'.format(zone),
                 '-cR', '{}'.format(red),
                 '-cG', '{}'.format(green),
                 '-cB', '{}'.format(blue)]
            )

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()



if __name__ == "__main__":
    app = App()
    app.start()

