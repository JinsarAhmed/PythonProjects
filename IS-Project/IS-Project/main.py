from tkinter import *

# from encryptDecrypt import EncryptDecrypt
from app import Activity
# from tte.emoji2 import *
from em.functional_email import *

class App:
	def __init__(self):
		self.root = Tk()
		self.root.title("App")


		can = Canvas(self.root, height=100, width=100,)
		can.place(relx=0.5, rely=0.5, anchor=CENTER)

		title = Label(can, text="LockBox", font= ("Arial", 25))

		description = Label(can, text="An multi-encryption App with Custom Secure Email App Integrated")
		credits = Label(can, text="Made By Jinsar (GL), Sarosh, Ali, Taha")
		
		# Creating Buttons
		b1 = Button(self.root, text="Cryptography", padx= 20, pady= 5, command=lambda: self.go(0))
		b2 = Button(self.root, text="Steganography", padx= 20, pady= 5, command=lambda: self.go(1))
		b3 = Button(self.root, text="Text-to-Emoji", padx= 20, pady= 5, command=lambda: self.go(2))
		b4 = Button(self.root, text="Custom Email App", padx= 20, pady= 5, command=lambda: self.go(3))


		title.pack(padx= 20, pady= 20)
		description.pack()
		credits.pack(pady=(0, 50))
		# b1.pack(padx= 10, pady= 10)
		# b2.pack(padx= 10, pady= 10)

		can.grid(row=0, column= 1)

		b1.grid(row=4, column=0, padx=(20, 0))
		b2.grid(row=4, column=1)
		b3.grid(row=4, column=2, padx=(0, 20))
		b4.grid(row=5, column=1, pady= 30)

		

		self.root.geometry("650x400")
		self.root.mainloop()

	def go(self, screen):
		self.root.destroy()
		
		if screen == 0:
			# EncryptDecrypt()
			import encryptDecrypt
		elif screen == 1:
			a = Activity()
			a.startLoop()
		elif screen == 2:
			from tte import emoji2
		elif screen == 3:
			root = Tk()
			obj = emails(root)
			root.mainloop()

if __name__=="__main__":
	App()