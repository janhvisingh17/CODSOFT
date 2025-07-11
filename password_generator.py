import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

# Create the database and table if not exists
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(GeneratedPassword TEXT NOT NULL);")
db.commit()
db.close()

class GUI():
    def __init__(self, master):
        self.master = master
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        root.title('Password Generator')
        root.geometry('600x400')
        root.config(bg='#003366')
        root.resizable(False, False)

        # Title
        Label(root, text="🔐 Password Generator 🔐", fg='white', bg='#003366', font='Helvetica 20 bold').pack(pady=20)

        # Input and output fields in a frame
        frame = Frame(root, bg='#003366')
        frame.pack(pady=10)

        # Password length
        Label(frame, text="Enter Password Length:", font='Helvetica 14', bg='#003366', fg='white').grid(row=0, column=0, sticky=W, pady=10)
        self.length_textfield = Entry(frame, textvariable=self.passwordlen, font='Helvetica 14', width=10)
        self.length_textfield.grid(row=0, column=1, padx=10)

        # Generated password field
        Label(frame, text="Generated Password:", font='Helvetica 14', bg='#003366', fg='white').grid(row=1, column=0, sticky=W, pady=10)
        self.generated_password_textfield = Entry(frame, textvariable=self.generatedpassword, font='Helvetica 14', fg='#FF4500', width=30)
        self.generated_password_textfield.grid(row=1, column=1, padx=10)

        # Buttons Frame
        btn_frame = Frame(root, bg='#003366')
        btn_frame.pack(pady=20)

        # Generate button
        Button(btn_frame, text="Generate Password", font='Helvetica 12 bold', bg='#28a745', fg='white',
               padx=10, pady=5, command=self.generate_pass).grid(row=0, column=0, padx=10)

        # Save button (disabled initially)
        self.save_button = Button(btn_frame, text="Save Password", font='Helvetica 12 bold', bg='#007BFF', fg='white',
                                  padx=10, pady=5, command=self.accept_fields, state=DISABLED)
        self.save_button.grid(row=0, column=1, padx=10)

        # Reset button
        Button(btn_frame, text="Reset", font='Helvetica 12 bold', bg='#6c757d', fg='white',
               padx=10, pady=5, command=self.reset_fields).grid(row=0, column=2, padx=10)

    def generate_pass(self):
        upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lower = list("abcdefghijklmnopqrstuvwxyz")
        chars = list("@#%&()\"?!")
        numbers = list("1234567890")

        try:
            length = int(self.length_textfield.get())
        except ValueError:
            messagebox.showerror("Error", "Password length must be a number")
            return

        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            return

        # Ensure character diversity
        u = random.randint(1, length - 3)
        l = random.randint(1, length - 2 - u)
        c = random.randint(1, length - 1 - u - l)
        n = length - u - l - c

        password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers, n)
        random.shuffle(password)
        gen_passwd = "".join(password)

        self.generatedpassword.set(gen_passwd)
        self.generated_password_textfield.delete(0, END)
        self.generated_password_textfield.insert(0, gen_passwd)
        self.save_button.config(state=NORMAL)

    def accept_fields(self):
        password = self.generatedpassword.get().strip()
        if not password:
            messagebox.showerror("Error", "Please generate a password before saving.")
            return

        try:
            with sqlite3.connect("users.db") as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO users(GeneratedPassword) VALUES (?)", (password,))
                db.commit()
            messagebox.showinfo("Success", "Password saved successfully!")
            self.save_button.config(state=DISABLED)
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def reset_fields(self):
        self.length_textfield.delete(0, END)
        self.generated_password_textfield.delete(0, END)
        self.generatedpassword.set('')
        self.passwordlen.set(0)
        self.save_button.config(state=DISABLED)

if __name__ == '__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()
