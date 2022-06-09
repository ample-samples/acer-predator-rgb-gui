#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import subprocess
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

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
                                              text="CustomTkinter",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="TEST SLIDER RED",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.print_red)
        self.button_1.grid(row=4, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="RGB3",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_3)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="RGB2",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_2)
        self.button_3.grid(row=2, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="RGB6",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_6)
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="rAnDoM",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.rgb_init_9)

        self.button_5.grid(row=6, column=0, pady=10, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left)
        self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
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

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

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
                                                       text="CTkButton 2",
                                                       command=self.button_event)
        self.slider_button_2.grid(row=7, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Save as")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Save preset",
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.radio_var = tkinter.IntVar(value=0)


        # RADIO BUTTONS, MODE SELECT
        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_0 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0,
                                                           text='Static')
        self.radio_button_0.grid(row=1, column=2, pady=5, padx=20, sticky="n")


        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1,
                                                           text='Breath')
        self.radio_button_1.grid(row=2, column=2, pady=5, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=2,
                                                           text='Neon' )
        self.radio_button_2.grid(row=3, column=2, pady=5, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=3,
                                                           text='Wave')
        self.radio_button_3.grid(row=4, column=2, pady=5, padx=20, sticky="n")




        # set default values
        self.radio_button_1.select()
        self.switch_2.select()
        self.slider_r.set(0)
        self.slider_g.set(0)
        self.slider_b.set(0)
        self.progressbar.set(0)
        # self.radio_button_3.configure(state=tkinter.DISABLED)

    def button_event(self):
        print("Button pressed")

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

#RETRIEVES THE VALUES OF THE R G AND B SLIDERS
    def set_colour(self):
        red = self.return_red()
        green = self.return_green()
        blue = self.return_blue()
        facer_path = '/home/todd/Programs/acer-predator-turbo-and-rgb-keyboard-linux-module/facer_rgb.py'
        mode = 0
        mode = self.radio_var.get()
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
    def print_red(self):
        print(str(self.red) + ' button')

    #NOT SURE WHAT THIS DOES, ONLY USING TO SATISFY command KWARG FROM self.mode_select, TAKEN FROM GITHUB EXAMPLE 
    def optionmenu_callback(choice):
        print("optionmenu dropdown clicked:", choice)

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
