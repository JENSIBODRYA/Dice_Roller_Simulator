#import modules
import tkinter
from PIL import Image, ImageTk
import random

#window design
root=tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')
root.configure(bg='white')


#welcome message
l1=tkinter.Label(root,text="WELCOME TO DICE ROLLER SIMULATOR",fg="#FE3939",bg='white',font="Helvetica 18 bold")
l1.pack()

#list of faces in dice
dice=['d1.jpg','d2.jpg','d3.jpg','d4.jpg','d5.jpg','d6.jpg']

#welcome page image
image = Image.open('dicen.png')
# The (450, 350) is (height, width)
image = image.resize((300, 350), Image.ANTIALIAS)
image2=ImageTk.PhotoImage(image)
# image2 = image.resize((200, 300), Image.ANTIALIAS)
label1=tkinter.Label(root,image=image2)
label1.image=image2
label1.pack(expand=True)

#function for rolling dice
def rolling_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1,bg='#B9C6C9')
    label1.image=image1

#button for roll the dice
button=tkinter.Button(root,text='Roll the Dice',font=('Arial,12,bold'),width=20,height=2,bg='#FE3939',fg='white',command=rolling_dice)

button.pack(expand=True)
#display the window command
root.mainloop()
