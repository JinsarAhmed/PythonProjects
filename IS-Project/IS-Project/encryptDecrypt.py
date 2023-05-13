from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) +
                     ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)

        dec.append(list_dec)
    return "".join(dec)


def Result():
    msg = Message.get()
    k= key.get()
    i = mode.get()
    if (i==1):
        Output.set(encode(k, msg))
    elif(i==2):
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo('Please Choose one of Encryption or Decrption. Try again.')


def Reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")
    

wn = Tk()
wn.geometry("500x500")
wn.configure(bg='yellow')
wn.title("Text Encryption")



Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

headingFrame1 = Frame(wn,bg="gray91",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.7,relheight=0.16)

headingLabel = Label(headingFrame1, text=" Welcome to Text Encryption and \n Decryption with Key", fg='grey19', font=('Courier',13,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


label1 = Label(wn, text='Enter the Message', font=('Courier',10))
label1.place(x=10,y=150)

msg = Entry(wn,textvariable=Message, width=35, font=('calibre',10,'normal'))
msg.place(x=200,y=150)

label2 = Label(wn, text='Enter the key', font=('Courier',10))
label2.place(x=10,y=200)

InpKey = Entry(wn, textvariable=key,  width=35,font=('calibre',10,'normal'))
InpKey.place(x=200,y=200)

label3 = Label(wn, text='Check one of encrypt or decrypt', font=('Courier',10))
label3.place(x=10,y=250)

Radiobutton(wn, text='Encrypt', variable=mode, value=1).place(x=100,y=300) 
Radiobutton(wn, text='Decrypt', variable=mode, value=2).place(x=200,y=300) 

label3 = Label(wn, text='Result', font=('Courier',10))
label3.place(x=10,y=350)

res = Entry(wn,textvariable=Output, width=35, font=('calibre',10,'normal'))
res.place(x=200,y=350)



ShowBtn = Button(wn,text="Show Message",bg='green', fg='black',width=15,height=1,command=Result)
ShowBtn['font'] = font.Font( size=12)
ShowBtn.place(x=180,y=400)

ResetBtn = Button(wn, text='Reset', bg='blue', fg='white', width=15,height=1,command=Reset)
ResetBtn['font'] = font.Font( size=12)
ResetBtn.place(x=15,y=400)

QuitBtn = Button(wn, text='Exit', bg='red', fg='white',width=15,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=12)
QuitBtn.place(x=345,y=400)


wn.mainloop()
