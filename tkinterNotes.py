from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420") #setting the size of our window
window.title("Hesham's first GUI!") # Changing the our window's title
# icon = PhotoImage(file="207255-wallpaper")
# window.iconphoto(True,icon)
window.config(background="black") # changing the background color of our 
# GUI[You can pick hex value of colours]
window.config(background="#33FF77") #using hex value to color.



#label = an area widget that holds text and/or an image within a window

label = Label(window,text="Hello world") # labeling our window
label = Label(window,
                text="I'm Hesham!", #setting text
                font=("Arial",40,"bold",), #configuring shape
                fg="green", #coloring the text 
                bg="black", #background color
                relief=RAISED, #boarder style
                bd=10, #boarder size
                padx=20,
                pady=20)


label.pack() #adding lable to our window [This will place our label on the center.]
label.place(x=0,y=0) #this will place our widget on the top left corner 
# [we can change the placement by changing the arguments]
label.place(x=100,y=100) #x will move it to right and y will move it to down



window.mainloop() # place window on computer screen, listen for events


