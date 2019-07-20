from tkinter import *
from textblob import TextBlob

root = Tk()

def sentiment():
    blob = TextBlob(e1_value.get())
    polar =  blob.polarity
    t1.delete('1.0', END)
    t1.insert(END, polar)


root.title('Sentiment Predictor')

label = Label(root,text = "Import your sentence here")
label.grid(row=0,column=0)

e1_value = StringVar()
e1= Entry(root,textvariable=e1_value)
e1.grid(row=0,column=1)

b1= Button(root,text = 'Compute Sentiment',command=sentiment)
b1.grid(row=0,column=2)

t1= Text(root,height=1,width=20)
t1.grid(row=0,column=3)








root.mainloop()
