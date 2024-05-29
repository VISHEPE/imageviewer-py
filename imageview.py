from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.geometry("700x700")

image_no_1 = ImageTk.PhotoImage(Image.open("Sample.png"))
image_no_2 = ImageTk.PhotoImage(Image.open("sample.png"))
image_no_3 = ImageTk.PhotoImage(Image.open("Sample.png"))
image_no_4 = ImageTk.PhotoImage(Image.open("sample.png"))

List_images = [image_no_1, image_no_2, image_no_3, image_no_4]

label = Label(image=image_no_1)
label.pack()

root.mainloop()