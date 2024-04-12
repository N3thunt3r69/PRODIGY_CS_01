import tkinter as tk
from tkinter import ttk

def caesar_cipher_N3thunt3r69(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (ord(char) - ord('a') + shift) % 26
                if mode == 'Decrypt':
                    shifted -= shift * 2
                result += chr((shifted % 26) + ord('a'))
            elif char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26
                if mode == 'Decrypt':
                    shifted -= shift * 2
                result += chr((shifted % 26) + ord('A'))
        else:
            result += char
    return result

def encrypt_decrypt_N3thunt3r69():
    message = entry_message.get()
    shift = int(entry_shift.get())
    mode = combobox_mode.get()

    if mode == 'Encrypt':
        result = caesar_cipher_N3thunt3r69(message, shift, 'Encrypt')
        label_result.config(text="N3thunt3r69_Encrypted message: " + result)
    elif mode == 'Decrypt':
        result = caesar_cipher_N3thunt3r69(message, shift, 'Decrypt')
        label_result.config(text="N3thunt3r69_Decrypted message: " + result)

# Create main window
root = tk.Tk()
root.title("N3thunt3r69's Caesar Cipher")
root.geometry("400x250")
root.configure(bg="#0d1117")

# Create frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame.configure(style="N3thunt3r69.TFrame")

# Change style to clam
style = ttk.Style()
style.theme_use("clam")

# Customize clam theme to have darker colors
style.configure("TLabel", background="#0d1117", foreground="white", font=("Arial", 11))
style.configure("TButton", background="#238636", foreground="white", font=("Arial", 11))
style.configure("TCombobox", background="#238636", foreground="white", font=("Arial", 11))
style.configure("N3thunt3r69.TFrame", background="#0d1117")

# Create message entry
label_message = ttk.Label(frame, text="The Message:")
label_message.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_message = ttk.Entry(frame, width=30)
entry_message.grid(row=0, column=1, padx=5, pady=5)

# Create shift entry
label_shift = ttk.Label(frame, text="Shift_Value:")
label_shift.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_shift = ttk.Entry(frame, width=10)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

# Create mode selection
label_mode = ttk.Label(frame, text="N3thunt3r69_Mode:")
label_mode.grid(row=2, column=0, padx=5, pady=5, sticky="w")
combobox_mode = ttk.Combobox(frame, values=["Encrypt", "Decrypt"], state="readonly")
combobox_mode.current(0)
combobox_mode.grid(row=2, column=1, padx=5, pady=5)

# Create encrypt/decrypt button
button_encrypt_decrypt = ttk.Button(frame, text="Encrypt/Decrypt", command=encrypt_decrypt_N3thunt3r69)
button_encrypt_decrypt.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create result label
label_result = ttk.Label(frame, text="")
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Set weight for resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Run the application
root.mainloop()
