#Timothy Nocks Final Project
#Website advertising a Tavern, with a menu, hours window, and an exit button
#3-10-24

#improt tkinter as well as pillow
import tkinter as tk
from PIL import ImageTk, Image

#Main Class for the website
class TavernWebsite:
    def __init__(self, master):
        #Create initial window
        self.master = master
        master.title("Tim's Tavern")

        #Display initial Image with a label while formating it to display correctly
        self.img1 = Image.open("img_tavern01.jpg")
        self.img1 = self.img1.resize((300, 125))
        self.photo1 = ImageTk.PhotoImage(self.img1)
        self.label1 = tk.Label(master, image=self.photo1)
        self.label1.pack()

        #Display second image the same way
        self.img2 = Image.open("img_food02.jpg")
        self.img2 = self.img2.resize((300, 125))
        self.photo2 = ImageTk.PhotoImage(self.img2)
        self.label2 = tk.Label(master, image=self.photo2)
        self.label2.pack()

        #Label for welcome messages, while changing their font and size
        self.tavern_label = tk.Label(master, text="Welcome to Tim's Tavern!", font=("Helvetica", 20))
        self.tavern_label.pack()
        self.tavern_label = tk.Label(master, text="Where the Beer is Cold and the Food is Colder", font=("Helvetica", 10))
        self.tavern_label.pack()
        self.tavern_label = tk.Label(master, text="Open since 130 B.C.", font=("Helvetica", 10))
        self.tavern_label.pack()

        #Button to display Menu
        self.menu_button = tk.Button(master, text="Menu", command=self.view_menu)
        self.menu_button.pack()

        #Button to display Hours
        self.menu_button = tk.Button(master, text="Hours", command=self.view_hours)
        self.menu_button.pack()

        #Button to Exit Program
        self.menu_button = tk.Button(master, text="Exit", command=self.close_window)
        self.menu_button.place(x=0, y=370)

    def view_menu(self):
        #function to display a seperate window with the menu, as well as information about how to order
        view_menu = tk.Toplevel(root)
        view_menu.title("Menu")
        view_menu.geometry("500x225")

        #lables to display information
        label = tk.Label(view_menu, text="Menu: ", font=("Helvetica", 20))
        label.pack()
        label = tk.Label(view_menu, text="1. Cheeseburger Dinner- $10", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_menu, text="2. Fried Chicken Dinner- $12", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_menu, text="3. Porkchop Dinner- $11", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_menu, text="4. Fish Dinner- $14", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_menu, text="5. Pasta Dinner- $13", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_menu, text="All dinners come with a choice of side (Fries, Tater Tots, or Onion Rings)", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_menu, text="Please call 123-123-1234 to place an order for carryout.", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_menu, text="The Kitchen stops accepting orders 1 hour before close.", font=("Helvetica", 10))
        label.pack()
    
    def view_hours(self):
        #function to display a second window with the hours the restuarant is open
        view_hours = tk.Toplevel(root)
        view_hours.title("Hours")
        view_hours.geometry("250x80")
        
        #labels to display information
        label = tk.Label(view_hours, text="Hours: ", font=("Helvetica", 20))
        label.pack()
        label = tk.Label(view_hours, text="Sunday-Thursday: 12pm-9pm", font=("Helvetica", 10))
        label.pack()
        label = tk.Label(view_hours, text="Friday-Saturday: 12pm-10pm", font=("Helvetica", 10))
        label.pack()
   
    def close_window(self):
        #function to close the window
        self.master.destroy()     

root = tk.Tk()
app = TavernWebsite(root)
root.mainloop()