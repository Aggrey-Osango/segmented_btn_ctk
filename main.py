# import tkinter as tk
import customtkinter as ctk
from tkinter import  *

c_radius, mid = 10, 0.5

widthx, heighty = 170, 30
btns = ["First Name", "Last Name", "Age"]
# app configuration
ctk.set_appearance_mode ("light")
ctk.set_default_color_theme ("blue")


# root window
root = ctk.CTk()
root.geometry("600x520")
root.title("Helium Notes")

# Frame for the window
frame = ctk.CTkFrame (master = root, width = 590, height = 510)

# variable text
var_text = StringVar ()
# first name entry obj
fname = ctk.CTkEntry (master = frame, width = widthx, height = heighty, placeholder_text = "First Name", corner_radius = c_radius )
lname = ctk.CTkEntry (master = frame, width = widthx, height = heighty, placeholder_text = "Last Name", corner_radius = c_radius)
age   = ctk.CTkEntry (master = frame, width = widthx, height = heighty, placeholder_text = "0", corner_radius = c_radius)

def log(value):
    ffname = str(fname.get ())
    llname = str (lname.get ())
    a = str (age.get ())
    if value == "First Name":
        var_text.set (f"First Name: {ffname}")

    if value == "Last Name":
        var_text.set (f"Last Name: {llname}")

    if value == "Age":
        var_text.set (f"Age: {a}")


msg_label = ctk.CTkLabel (master = frame, width = widthx, height = heighty, corner_radius = c_radius, textvariable = var_text, bg_color = "yellow")

seg_btn = ctk.CTkSegmentedButton (master = frame, width = widthx, height = heighty, corner_radius = c_radius, values = btns, command = log)

frame.pack  (padx=10, pady = 10)
fname.place (relx = mid, rely = 0.2 , anchor = CENTER)
lname.place (relx = mid, rely = 0.3, anchor = CENTER)
age.place   (relx = mid, rely = 0.4, anchor = CENTER)
seg_btn.place (relx = mid, rely = 0.5, anchor = CENTER)
msg_label.place(relx = mid, rely =0.6, anchor = CENTER)

if __name__ == '__main__':
    root.mainloop()
