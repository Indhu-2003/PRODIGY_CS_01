import tkinter as tk

def caesar_encrypt(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)

def encrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())

    encrypted_message = caesar_encrypt(message, shift)
    label_encrypted.config(text="Encrypted message: " + encrypted_message)

def decrypt_message():
    encrypted_message = entry_encrypted.get()
    shift = int(entry_shift.get())

    decrypted_message = caesar_decrypt(encrypted_message, shift)
    label_decrypted.config(text="Decrypted message: " + decrypted_message)

# GUI setup
window = tk.Tk()
window.title("Caesar Cipher Encryption & Decryption")

# Message input
label_message = tk.Label(window, text="Enter your message:")
label_message.grid(row=0, column=0, padx=5, pady=5)
entry_message = tk.Entry(window)
entry_message.grid(row=0, column=1, padx=5, pady=5)

# Shift value input
label_shift = tk.Label(window, text="Enter the shift value:")
label_shift.grid(row=1, column=0, padx=5, pady=5)
entry_shift = tk.Entry(window)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

# Encrypt button
btn_encrypt = tk.Button(window, text="Encrypt", command=encrypt_message)
btn_encrypt.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Encrypted message display
label_encrypted = tk.Label(window, text="")
label_encrypted.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Encrypted message input
label_encrypted_input = tk.Label(window, text="Enter encrypted message:")
label_encrypted_input.grid(row=4, column=0, padx=5, pady=5)
entry_encrypted = tk.Entry(window)
entry_encrypted.grid(row=4, column=1, padx=5, pady=5)

# Decrypt button
btn_decrypt = tk.Button(window, text="Decrypt", command=decrypt_message)
btn_decrypt.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Decrypted message display
label_decrypted = tk.Label(window, text="")
label_decrypted.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
