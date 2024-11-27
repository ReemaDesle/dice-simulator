import tkinter as tk
from tkinter import Label, Button
from tkinter import PhotoImage
import random
from PIL import Image, ImageTk

def roll_dice(sides):

    # Create a new window for displaying the result(Result Window)
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    width=600
    height=400
    scr_width=result_window.winfo_screenwidth()
    scr_height=result_window.winfo_screenheight()
    x=(scr_width/2)-(width/2)
    y=(scr_height/2)-(height/2)
    result_window.geometry('%dx%d+%d+%d' %(width,height,x,y))
    result_window.resizable(False,False)
    result_window.config(bg='#bedef4')
    
    # Roll the dice
    result1 = random.randint(1, sides)
    result2 = random.randint(1, sides)
    
    # Display the image of the dice for result1
    image_path1= f"C:\\Dice_Game\\die_{sides}_face_{result1}.jpeg"
    image1 = Image.open(image_path1)
    photo1 = ImageTk.PhotoImage(image1)
    image_label1 = tk.Label(result_window, image=photo1)
    image_label1.image = photo1
    image_label1.grid(row=0,column=0,padx=10,pady=20)
    
    # Display the image of the dice for result2
    image_path2=f"C:\\Dice_Game\\die_{sides}_face_{result2}.jpeg"
    image2 = Image.open(image_path2)
    photo2 = ImageTk.PhotoImage(image2)
    image_label2 = tk.Label(result_window, image=photo2)
    image_label2.image = photo2
    image_label2.grid(row=0,column=1,padx=30,pady=40)
    
    #Display congratulations text
    total = result1 + result2
    label1 = tk.Label(result_window, text=f'Congratulations! You got: {result1} and {result2}', anchor='center',font=('Arial',16))
    label2 = tk.Label(result_window, text=f'Your Total is: {total}', anchor='center', font=('Arial',16))
    label1.grid(row=1,column=0,columnspan=2)
    label2.grid(row=2,column=0,columnspan=2)

def choose_dice(sides):
    # Hide the main window
    root.withdraw()
    
    # Create a new window for choosing the dice
    choose_window = tk.Toplevel(root)
    choose_window.title("Choose Dice")
    #choose_window.maxsize(600,400)
    width=500
    height=300
    scr_width=choose_window.winfo_screenwidth()
    scr_height=choose_window.winfo_screenheight()
    x=(scr_width/2)-(width/2)
    y=(scr_height/2)-(height/2)
    choose_window.geometry('%dx%d+%d+%d' %(width,height,x,y))
    choose_window.resizable(False,False)
    choose_window.config(bg='#bedef4')
    
    # Button to roll the dice
    roll_button = tk.Button(choose_window, text="Roll!", command=lambda: roll_dice(sides), width=10, height=2)
    roll_button.pack(pady=100,side='top',anchor='center')
    

# Main window
root = tk.Tk()
root.title("Dice Simulator")
width=800
height=400
scr_width=root.winfo_screenwidth()
scr_height=root.winfo_screenheight()
x=(scr_width/2)-(width/2)
y=(scr_height/2)-(height/2)
root.geometry('%dx%d+%d+%d' %(width,height,x,y))
root.resizable(False,False)
root.config(bg='#bedef4')
# Text labels
tk.Label(root, text="Choose the number of faces for the dice:", font=("Arial", 16)).pack(pady=30)

# Buttons for choosing dice
tk.Button(root, text="6 faced die", command=lambda: choose_dice(6),width=10, height=2).pack(pady=40)
tk.Button(root, text="8 faced die", command=lambda: choose_dice(8),width=10,height=2).pack(pady=40)

root.mainloop()
