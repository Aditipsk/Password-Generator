import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password():
    password_length = length_entry.get()
    if password_length.isdigit() and int(password_length) > 0:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(int(password_length)))
        password_label.config(text=f"Generated Password: {password}", font=("Helvetica", 20))
    else:
        password_label.config(text="Invalid length. Please enter a positive integer.", font=("Helvetica", 20))

root = tk.Tk()
root.title("Password Generator")
root.geometry("800x600")
root.configure(bg="#F0F0F0")  # Light gray background

main_frame = ttk.Frame(root, padding=40)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(main_frame, text="Password Generator", font=("Helvetica", 36, "bold"), foreground="#333333")
title_label.pack(pady=20)

length_label = ttk.Label(main_frame, text="Password Length:", font=("Helvetica", 24), foreground="#333333")
length_label.pack(pady=10)

length_entry = ttk.Entry(main_frame, font=("Helvetica", 24), width=10)
length_entry.pack()

generate_button = ttk.Button(main_frame, text="Generate", command=generate_password, style="Accent.TButton")
generate_button.pack(pady=20)

password_label = ttk.Label(main_frame, text="", font=("Helvetica", 20), foreground="#333333")
password_label.pack(pady=20)

style = ttk.Style()
style.theme_use("clam")
style.configure("Accent.TButton", background="#4CAF50", foreground="#FFFFFF", font=("Helvetica", 24))

root.mainloop()