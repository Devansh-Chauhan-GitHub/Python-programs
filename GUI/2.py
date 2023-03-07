from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("900x500")
root.minsize(200,200)
root.maxsize(1800,1000)
image=Image.open("Wallpaper.jpg")
photo=ImageTk.PhotoImage(image)
#image=Image
#Image=ImageTk.open("Wallpaper.jpg")
# photo=PhotoImage(file="Wallpaper.png")
image_Label=Label(image=photo)
image_Label.pack()
root.mainloop()