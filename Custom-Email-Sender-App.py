import tkinter as tk
from tkinter import messagebox
import smtplib

class PhishingSimulator:
    def __init__(self):
        self.sender_email = "jinsar456shaikh@gmail.com"
        self.sender_password = "gepyvtzosnmyjpek"
        self.target_email = "hjbusiness456@gmail.com"
        self.subject = "hehe"
        self.message = "test hai bhai"

    def run(self):
        root = tk.Tk()
        root.title("Phishing Simulator")

        email_label = tk.Label(root, text="Target Email:")
        email_label.pack()

        email_entry = tk.Entry(root)
        email_entry.pack()

        subject_label = tk.Label(root, text="Email Subject:")
        subject_label.pack()

        subject_entry = tk.Entry(root)
        subject_entry.pack()

        message_label = tk.Label(root, text="Email Message:")
        message_label.pack()

        message_text = tk.Text(root)
        message_text.pack()

        button = tk.Button(root, text="Send Phishing Email", command=lambda: self.send_phishing_email(email_entry.get(), subject_entry.get(), message_text.get("1.0", "end-1c")))
        button.pack()

        root.mainloop()

    def send_phishing_email(self, target_email, subject, message):
        self.target_email = target_email
        self.subject = subject
        self.message = message

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.target_email, f"Subject: {self.subject}\n\n{self.message}")
            server.quit()
            messagebox.showinfo("Email Status", "Phishing email sent successfully!")
        except Exception as e:
            messagebox.showerror("Email Status", f"Error sending phishing email: {e}")

if __name__ == "__main__":
    phishing_simulator = PhishingSimulator()
    phishing_simulator.run()
