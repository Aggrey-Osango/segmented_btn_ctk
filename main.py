# import tkinter as tk
import customtkinter as ctk
from tkinter import  *

c_radius = 10
mid = 0.5
widthx, heighty = 170, 30

# app configuration
ctk.set_appearance_mode ("light")
ctk.set_default_color_theme ("#8AAB93")


# root window
root = ctk.CTk()
root.geometry("600x520")
root.title("Helium Notes")

# Frame for the window
frame = ctk.CTkFrame (master = root, width = 590, height = 510)

# first name entry obj
fname = ctk.CTk.Entry (master = frame, width = widthx, height = heighty, placeholder_text = "First Name", corner_radius = c_radius )
lname = ctk.CTk.Entry (master = frame, width = widthx, height = heighty, placeholder_text = "Last Name", corner_radius = c_radius)
age   = ctk.CTk.Entry (master = frame, widthx= widthx, height = heighty, placeholder_text = "0", corner_radius = c_radius)


frame.pack  (padx=10, pady = 10)
fname.place (relx = mid, rely = mid - 0.2, anchor = CENTER)
lname.place (relx = mid, rely = mid + 0.1, anchor = CENTER)
age.place   (relx = mid, rely = mid + 0.2, anchor = CENTER)


if __name__ == '__main__':
    root.mainloop()
