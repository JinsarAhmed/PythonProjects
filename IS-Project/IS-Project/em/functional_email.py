import tkinter
import webbrowser
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, filedialog
import os
import pandas as pd
import em.email_function as email_function
import time
import em.email_function2 as email_function2



class emails:

    def __init__(self, root):
        self.root = root
        self.root.title("Custom Email App")
        self.root.geometry("1000x550+200+50")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        self.settings_icon = ImageTk.PhotoImage(file="./em/Settings.png")
        title = Label(self.root, text="Custom Email App", font=("Goudy Old Style", 48, "bold"), bg="#ADD8E6",
                      fg="black").place(x=0, y=0, relwidth=1)

        button_setting = Button(self.root, image=self.settings_icon, bd=0, activebackground="#ADD8E6", bg="#ADD8E6",
                                cursor="hand2", command=self.setting_window).place(x=900, y=5)

        description = Label(self.root, text="An application of LockBox App", font=("Valibri(Body)", 14), bg="#FFD966",
                            fg="black").place(x=0, y=90, relwidth=1)

        self.var_choice = StringVar()
        single = Radiobutton(self.root, text="Single", value="single", variable=self.var_choice,
                             activebackground="white",
                             command=self.check_single_or_bulk, font=("times new roman", 30, "bold"), bg="white",
                             fg="#262626").place(x=50, y=150)
        Bulk = Radiobutton(self.root, text="Bulk", value="bulk", variable=self.var_choice, activebackground="white",
                           command=self.check_single_or_bulk, font=("times new roman", 30, "bold"), bg="white",
                           fg="#262626").place(x=250, y=150)

        self.var_choice.set("single")

        to = Label(self.root, text="To (Email Address)", font=("times new roman", 18), bg="white").place(x=50, y=250)
        sub = Label(self.root, text="SUBJECT", font=("times new roman", 18), bg="white").place(x=50, y=300)
        msg = Label(self.root, text="MESSAGE", font=("times new roman", 18), bg="white").place(x=50, y=350)

        self.txt_to = Entry(self.root, font=("times new roman", 14), bg="lightyellow")
        self.txt_to.place(x=300, y=250, width=350, height=30)

        self.button_browse = Button(self.root, command=self.browse_file, text="Browse",
                                    font=("times new roman ", 15, "bold"), bg="#8FAADC", fg="#262626",
                                    activebackground="#262626", activeforeground="#262626", cursor="hand2",
                                    state=DISABLED)

        self.button_browse.place(x=670, y=250, width=120, height=30)

        self.txt_sub = Entry(self.root, font=("times new roman", 14), bg="lightyellow")
        self.txt_sub.place(x=300, y=300, width=450, height=30)

        self.txt_msg = Text(self.root, font=("times new roman", 14), bg="lightyellow")
        self.txt_msg.place(x=300, y=350, width=650, height=120)

        self.lbl_total = Label(self.root, font=("times new roman", 18), bg="white")
        self.lbl_total.place(x=50, y=490)

        self.lbl_sent = Label(self.root, font=("times new roman", 18), bg="white", fg="green")
        self.lbl_sent.place(x=300, y=490)

        self.lbl_left = Label(self.root, font=("times new roman", 18), bg="white", fg="orange")
        self.lbl_left.place(x=420, y=490)

        self.lbl_failed = Label(self.root, font=("times new roman", 18), bg="white", fg="red")
        self.lbl_failed.place(x=550, y=490)

        # self.button_attach = Button(self.root, command=self.add_attachments, text="Read Attachment",
        #                             font=("times new roman ", 13, "bold"), bg="#8FAADC", fg="#262626",
        #                             activebackground="#262626", activeforeground="#262626", cursor="hand2")
        #
        # self.button_attach.place(x=670, y=490, width=160, height=30)

        self.button_browse2 = Button(self.root, command=self.attachFiles, text="Send Attachment",
                                     font=("times new roman ", 13, "bold"), bg="orange", fg="#262626",
                                     activebackground="#262626", activeforeground="#262626", cursor="hand2")

        self.button_browse2.place(x=770, y=300, width=180, height=30)



        button_send = Button(self.root, command=self.send_email, text="SEND", font=("times new roman ", 18, "bold"),
                             bg="#00B0F0", fg="white",
                             activebackground="#262626", activeforeground="white", cursor="hand2").place(x=830, y=490,
                                                                                                         width=120,
                                                                                                         height=30)
        button_clear = Button(self.root, text="CLEAR", command=self.clear1, font=("times new roman ", 18, "bold"),
                              bg="#262626", fg="white",
                              activebackground="#00B0F0", activeforeground="white", cursor="hand2").place(x=700, y=490,
                                                                                                          width=120,
                                                                                                            height=30)

        self.check_file_exist()

    # def add_files(self):
    #     email_attach = email_function2.attachm()

    def attachFiles(self):
        if self.var_choice.get() == "single":

            email_attach = email_function2.attach_single(self.txt_to.get(), self.txt_sub.get(), self.txt_msg.get('1.0', END),
                                                  self.from_email, self.password)

            if email_attach == "s":
                messagebox.showinfo("Success", "Email has been sent", parent=self.root)
            if email_attach == "f":
                messagebox.showerror("Error", "Email not sent", parent=self.root)

        if self.var_choice.get() == "bulk":
            email_attach = email_function2.attach_mul(self.txt_to.get(), self.txt_sub.get(), self.txt_msg.get('1.0', END),
                                                  self.from_email, self.password)

            if email_attach == "s":
                messagebox.showinfo("Success", "Email has been sent", parent=self.root)
            if email_attach == "f":
                messagebox.showerror("Error", "Email not sent", parent=self.root)

    def add_attachments(self):
        if self.var_choice.get() == "single":
            status2 = email_function2.email_send_funct_next(self.txt_to.get(), self.txt_sub.get(),
                                                            self.txt_msg.get('1.0', END),
                                                            self.from_email, self.password)

            if status2 == "s":
                messagebox.showinfo("Success", "Email has been sent", parent=self.root)
            if status2 == "f":
                messagebox.showerror("Error", "Email not sent", parent=self.root)

        if self.var_choice.get() == "bulk":
            status2 = email_function2.email_send_funct_next(self.txt_to.get(), self.txt_sub.get(),
                                                            self.txt_msg.get('1.0', END), self.from_email,
                                                            self.password)
            if status2 == "s":
                messagebox.showinfo("Success", "Email has been sent", parent=self.root)
            if status2 == "f":
                messagebox.showerror("Error", "Email not sent", parent=self.root)

    def browse_file(self):
        op = filedialog.askopenfile(initialdir='/', title="Select Excel File For Emails",
                                    filetypes=(("All Files", "*.*"), ("Excel files", ".xlsx")))
        if op != None:
            data = pd.read_excel(op.name)
            if 'Email' in data.columns:
                self.emails = list(data['Email'])
                c = []
                for i in self.emails:
                    if pd.isnull(i) == False:
                        c.append(i)
                self.emails = c
                if len(self.emails) > 0:
                    self.txt_to.config(state=NORMAL)
                    self.txt_to.delete(0, END)
                    self.txt_to.insert(0, str(op.name.split("/")[-1]))
                    self.txt_to.config(state='readonly')
                    self.lbl_total.config(text="Total: " + str(len(self.emails)))
                    self.lbl_sent.config(text="SENT: ")
                    self.lbl_left.config(text="LEFT: ")
                    self.lbl_failed.config(text="SUCCESS: ")
                else:
                    messagebox.showerror("Error", "This file doesn't have any emails", parent=self.root)
            else:
                messagebox.showerror("Error", "Please Select file which has Email Columns", parent=self.root)

    def send_email(self):
        x = len(self.txt_msg.get('1.0', END))
        if self.txt_to.get() == "" or self.txt_sub.get() == "" or x == 1:
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            if self.var_choice.get() == "single":
                status = email_function.email_send_funct(self.txt_to.get(), self.txt_sub.get(),
                                                         self.txt_msg.get('1.0', END), self.from_email, self.password)
                if status == "s":
                    messagebox.showinfo("Success", "Email has been sent", parent=self.root)
                if status == "f":
                    messagebox.showerror("Error", "Email not sent", parent=self.root)
            if self.var_choice.get() == "bulk":
                self.failed = []
                self.s_count = 0
                self.f_count = 0
                for x in self.emails:
                    status = email_function.email_send_funct(x, self.txt_sub.get(), self.txt_msg.get('1.0', END),
                                                             self.from_email, self.password)
                    if status == "s":
                        self.s_count += 1
                    if status == "f":
                        self.f_count += 1
                    self.status_bar()
                    time.sleep(1)
                messagebox.showinfo("Success", "EMAIL HAS BEEN SENT, Please Check", parent=self.root)

    def status_bar(self):
        self.lbl_total.config(text="STATUS: " + str(len(self.emails)) + "=>>")
        self.lbl_sent.config(text="SENT: " + str(self.s_count))
        self.lbl_left.config(text="LEFT: " + str(len(self.emails) - (self.s_count + self.f_count)))
        self.lbl_failed.config(text="SUCCESS: " + str(self.s_count))
        self.lbl_total.update()
        self.lbl_sent.update()
        self.lbl_left.update()
        self.lbl_failed.update()

    def check_single_or_bulk(self):
        if self.var_choice.get() == "single":
            self.button_browse.config(state=DISABLED)
            self.txt_to.config(state=NORMAL)
            self.txt_to.delete(0, END)
            self.clear1()
        if self.var_choice.get() == "bulk":
            self.button_browse.config(state=NORMAL)
            self.txt_to.delete(0, END)
            self.txt_to.config(state='readonly')

    def clear1(self):
        self.txt_to.config(state=NORMAL)
        self.txt_to.delete(0, END)
        self.txt_sub.delete(0, END)
        self.txt_msg.delete('1.0', END)
        self.var_choice.set("single")
        self.button_browse.config(state=DISABLED)
        self.lbl_total.config(text="")
        self.lbl_sent.config(text="")
        self.lbl_left.config(text="")
        self.lbl_failed.config(text="")

    def setting_window(self):
        self.check_file_exist()
        self.root2 = Toplevel()
        self.root2.title("Settings")
        self.root2.geometry("700x350+350+90")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.config(bg="white")

        title2 = Label(self.root2, text="Credentials Settings", font=("Goudy Old Style", 48, "bold"), bg="#ADD8E6",
                       fg="black").place(x=0, y=0, relwidth=1)
        description2 = Label(self.root2,
                             text="Enter the Email address and password from which you want to send all emails",
                             font=("Calibri(Body)", 14), bg="#FFD966",
                             fg="black").place(x=0, y=90, relwidth=1)
        from_email = Label(self.root2, text="Email Address", font=("times new roman", 18), bg="white").place(x=50,
                                                                                                             y=150)
        password = Label(self.root2, text="PASSWORD", font=("times new roman", 18), bg="white").place(x=50, y=200)

        self.txt_from = Entry(self.root2, font=("times new roman", 14), bg="lightyellow")
        self.txt_from.place(x=250, y=150, width=330, height=30)

        self.txt_pass = Entry(self.root2, font=("times new roman", 14), bg="lightyellow", show="*")
        self.txt_pass.place(x=250, y=200, width=330, height=30)

        button_redirect = Button(self.root2, command=self.button_redirect, text="Click to enable ",
                                 font=("times new roman ", 18, "bold"),
                                 bg="red", fg="white",
                                 activebackground="#262626", activeforeground="white", cursor="hand2").place(x=50,
                                                                                                             y=260,
                                                                                                             width=200,
                                                                                                             height=30)

        button_save = Button(self.root2, command=self.save_setting, text="SAVE", font=("times new roman ", 18, "bold"),
                             bg="#00B0F0", fg="white",
                             activebackground="#262626", activeforeground="white", cursor="hand2").place(x=430, y=260,
                                                                                                         width=120,
                                                                                                         height=30)
        button_clear2 = Button(self.root2, command=self.clear2, text="CLEAR", font=("times new roman ", 18, "bold"),
                               bg="#262626", fg="white",
                               activebackground="#00B0F0", activeforeground="white", cursor="hand2").place(x=300, y=260,
                                                                                                           width=120,
                                                                                                           height=30)
        self.txt_from.insert(0, self.from_email)
        self.txt_pass.insert(0, self.password)

    def clear2(self):
        self.txt_from.delete(0, END)
        self.txt_from.delete(0, END)

    def check_file_exist(self):
        if os.path.exists("cred.txt") == False:
            f = open('cred.txt', 'w')
            f.write(",")
            f.close()
        f2 = open('cred.txt', 'r')
        self.credentials = []
        for i in f2:
            self.credentials.append([i.split(",")[0], i.split(",")[1]])
        self.from_email = self.credentials[0][0]
        self.password = self.credentials[0][1]

    def button_redirect(self):
        new = 1
        url = "https://myaccount.google.com/security"
        webbrowser.open(url, new=new)

    def save_setting(self):
        if self.txt_from.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            f = open('cred.txt', 'w')
            f.write(self.txt_from.get() + "," + self.txt_pass.get())
            f.close()
            messagebox.showinfo("Success", "SAVED SUCCESSFULLY", parent=self.root2)
            self.check_file_exist()


# root = Tk()
# obj = emails(root)
# root.mainloop()
