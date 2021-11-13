from tkinter import*
def onSubmitButtonClicked():
      #print("Yay!It works!")
      daysAttendedNum=int(daysAttendedString.get())
      if daysAttendedNum==4:
        print(nameString.get(), "is elligible for certificate")
        resultString.set("{} is eligible for the certificate".format(nameString.get()))
      else:
        print(nameString.get(),"is not eligible for certificate")
        resultString.set("{} is not eligible for certificate".format(nameString.get()))
def onClearButtonClicked():
      nameString.set("")
      daysAttendedString.set("")
      resultString.set("")

def onExitButtonClicked():
      root.destroy()

root=Tk()
root.title("My First GUI Application")
root.geometry("%dx%d+0+0"%(400,250))

bootcampMessage=Label(text ="Welcome to the Bootcamp")
bootcampMessage.pack()
todaysTopic=Label(text="we are learning Tkinter")
todaysTopic.pack()

#Taking in values in the form
nameLabel=Label(text = "Enter your name: ")
nameLabel.place(x=20,y=50)

daysAttended=Label(text= "Enter the number of days attended:")
daysAttended.place(x=20,y=70)

#Taking in values from the user
nameString=StringVar()
nameEntry =Entry(root,textvariable = nameString)
nameEntry.place(x=240,y=50)

daysAttendedString=StringVar()
daysAttendedEntry=Entry(root,textvariable= daysAttendedString)
daysAttendedEntry.place(x=240,y=70)

resultString=StringVar()
result=Entry(root,textvariable=resultString,width=50).place(x=40,y=100)

#Placing buttons
submitButton=Button(text ="Submit",command=onSubmitButtonClicked)
submitButton.place(x=100,y=150)
clearButton=Button(text="Clear",command=onSubmitButtonClicked)
clearButton.place(x=150,y=150)
exitButton=Button(text="Exit", command=onExitButtonClicked)
exitButton.place(x=190,y=150)
root.mainloop()
