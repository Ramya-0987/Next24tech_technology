import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")

# Labels
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Password").grid(row=3, column=0, padx=10, pady=10)

# Entry fields
name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

name_entry.grid(row=0, column=1, padx=10, pady=10)
age_entry.grid(row=1, column=1, padx=10, pady=10)
email_entry.grid(row=2, column=1, padx=10, pady=10)
password_entry.grid(row=3, column=1, padx=10, pady=10)

# Submit button function
def submit():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if name and age and email and password:
        messagebox.showinfo("Registration Successful", f"Welcome, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()




