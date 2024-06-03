import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_text():
    text = text_entry.get()
    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Xato", "Kalit butun son bo'lishi kerak.")
        return
    encrypted = caesar_encrypt(text, shift)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, encrypted)

def decrypt_text():
    text = text_entry.get()
    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Xato", "Kalit butun son bo'lishi kerak.")
        return
    decrypted = caesar_decrypt(text, shift)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, decrypted)

root = tk.Tk()
root.title("Caesar Shifrlash/Deshifrlash")

# Set the size of the window and add a background color
root.geometry("500x250")
root.configure(bg="#f0f0f0")

# Add a title label with a larger font
title_label = tk.Label(root, text="Caesar Shifrlash/Deshifrlash", font=("Algerian", 16, "bold"), bg="#f0f0f0")
title_label.grid(row=0, columnspan=2, pady=10)

# Adjusting the labels and entries
tk.Label(root, text="Matnni kiriting:", font=("Algerian", 12), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
text_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
text_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Kalit:", font=("Algerian", 12), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="e")
key_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
key_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Add encrypt and decrypt buttons with a bit of padding and larger font
encrypt_button = tk.Button(root, text="Shifrlash", command=encrypt_text, font=("Algerian", 12), bg="#4caf50", fg="white")
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Deshifrlash", command=decrypt_text, font=("Algerian", 12), bg="#f44336", fg="white")
decrypt_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Natija:", font=("Algerian", 12), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10, sticky="e")
result_entry = tk.Entry(root, width=50, font=("Algerian", 12))
result_entry.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
