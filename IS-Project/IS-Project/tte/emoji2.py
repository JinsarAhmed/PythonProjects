import pandas as pd
import random
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

emoji = pd.read_excel("./tte/emoji.xlsx")
my_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ',',','.','<','>','/','?',"'",'"',';',':','1','2','3','4','5','6','7','8','9','0','\\','|','[',']','{','}','+','=','-','_',')','(','*','&','^','%','$','#','@','!','~','`']

def encod(sen):
    ln = len(sen)
    b = sen[::-1]
    if(ln%2==0):
        ln_h = int(ln/2)
        a_a = b[:ln_h]
        a_b = b[ln_h:]
    else:
        ln_h = int(ln/2)
        a_a = b[:ln_h]
        a_b = b[ln_h:]
    a_a = a_a[::-1]
    res = a_a + a_b
    return(res)

def sentence_input(inp):
    if(len(inp) !=0):
        li = list(inp) 
        an_list=[]
        st = random.randint(0,444)
        an_list.append(emoji.iloc[st,0])
        s = pd.Series(li)
        r = s.isin(emoji['emj'])
        if(r.any(axis = 0)==True):
            
            inn = False
            for i in range(len(li)):
                
                s_in = pd.Series(list(li[i]))
                r_in = s_in.isin(emoji['emj'])
                
                if(r_in.values==True):
                    if(inn!= True):
                        inn = True
                        an_list.append('♪')
                    an_list.append(li[i])
                else:
                    if(inn== True):
                        inn = False
                        an_list.append('♫')
                    pos = my_list.index(li[i])
                    pos = pos + st
                    an_list.append(emoji.iloc[pos,0])               
        else:
            for i in range(len(li)):
                pos = my_list.index(li[i])
                pos = pos + st
                an_list.append(emoji.iloc[pos,0])
        output='' 
        for x in an_list: 
                output += x
        output = encod(output)
        return(output)
    else:
        return("Wrong input !")
    
def decod(sen):
    ln = len(sen)
    if(ln%2==0):
        ln_h = int(ln/2)
        a_a = sen[ln_h:]
        a_b = sen[:ln_h]
    else:
        ln_h = int(ln/2)
        a_a = sen[ln_h:]
        a_b = sen[:ln_h]
    a_a = a_a[::-1]
    final = a_a + a_b
    return(final)

def emoji_input(einp):
    einp = decod(einp)
    if(len(einp)>=2):
        sent=''
        val = emoji.loc[emoji['emj']==einp[0]].index[0]
        i=1
        while(True):
            if(einp[i]=='♪'):
                for j in range(i+1,len(einp)):
                    if(einp[j]=='♫'):
                        break
                    else:
                        sent += einp[j]
                i=j
            else:
                d = emoji.loc[emoji['emj']==einp[i]].index[0]
                sent+= my_list[d-val]
            if((i+1)>=len(einp)):
                break
            else:
                i+=1
        return(sent)
    else:
        return('Wrong input !')
    

window = tk.Tk()
window.title("Emoji Encoder/Decoder")

# Create labels and text boxes
input_label = ttk.Label(window, text="Enter text:")
input_label.grid(column=0, row=0, padx=10, pady=10)
input_box = ttk.Entry(window, width=50)
input_box.grid(column=1, row=0, padx=10, pady=10)

output_label = ttk.Label(window, text="Output:")
output_label.grid(column=0, row=1, padx=10, pady=10)
output_box = scrolledtext.ScrolledText(window, width=50, height=5)
output_box.grid(column=1, row=1, padx=10, pady=10)

def encode_text():
    input_text = input_box.get()
    output_text = sentence_input(input_text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output_text)

def decode_text():
    input_text = input_box.get()
    output_text = emoji_input(input_text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output_text)

# Create buttons
encode_button = ttk.Button(window, text="Encode", command=encode_text, style='Red.TButton')
encode_button.grid(column=0, row=2, padx=10, pady=10)

decode_button = ttk.Button(window, text="Decode", command=decode_text, style='Green.TButton')
decode_button.grid(column=1, row=2, padx=10, pady=10)

style = ttk.Style()
style.configure("Red.TButton", foreground="red", background="red")
style.configure("Green.TButton", foreground="green", background="green")


title_label = tk.Label(window, text="Text-to-Emoji Encryption and Decryption", bg="yellow", font=("Arial", 18))
title_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Run the window
window.mainloop()
