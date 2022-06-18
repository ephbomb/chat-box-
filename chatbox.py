from tkinter import *
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
text = Text(root,bg='blue', fg='white')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='deeppink', fg='white', width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('chat')
root.mainloop()
