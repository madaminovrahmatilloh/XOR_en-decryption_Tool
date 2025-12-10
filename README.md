# XOR Encryption Tool

A simple yet powerful Python tool for **XOR encryption and decryption** of text and files.  
Supports text, `.docx`, `.pdf`, `.exe`, images, and any other file type.

---

## Features

- Encrypt and decrypt **text** with a key.
- Encrypt and decrypt **files** with a key.
- Smart file mode: automatically detects `.xor` files for decryption.
- Works on **Windows, Linux, and WSL**.
- Drag-and-drop paths supported on Windows.
- No external libraries required — only **Python 3.x**.

---

## Usage

### 1. Run the tool

    python XOR_encryption.py
### 2. Menu options

1. Encrypt Text – type text and key to encrypt
2. Decrypt Text – input encrypted hex and key to decrypt
3. Encrypt/Decrypt File – drag-and-drop or type full path of a file
4. Exit – quit the program

---

## 3. File Paths & Location Fix

If you get “File not found!”, it usually means Python cannot locate the file.
Here’s how to provide the correct path depending on your setup:

### A. Running in Windows (CMD/PowerShell)

- Drag your file into the terminal or copy its full path from Explorer
- Quotes will be stripped automatically
- Example: 
  C:\Users\asus\Downloads\Cybersecurity_Projects_1_to_550.docx

- Python will handle backslashes automatically

---

### B. Running in WSL / Ubuntu / VS Code with WSL

- Windows drives are mounted under /mnt/
- Convert your Windows path from:

C:\Users\asus\Downloads\Cybersecurity_Projects_1_to_550.docx

to WSL style:

/mnt/c/Users/asus/Downloads/Cybersecurity_Projects_1_to_550.docx

- Drag-and-drop might work in some terminals, but you may need to manually replace `C:\` with `/mnt/c/`
- Always verify the file exists in WSL with:

ls /mnt/c/Users/asus/Downloads/

---

## 4. How it works

- Uses XOR encryption with a key of your choice
- Works on any file type
- Encrypted files get .xor appended
- Decrypted files get _decrypted appended

---

## Requirements

- Python 3.x
- No additional libraries required

---

## Example
Choose option (1/2/3/4): 3

Enter full file path: /mnt/c/Users/asus/Downloads/example.docx

Enter key: mysecretkey

File encrypted successfully: /mnt/c/Users/asus/Downloads/example.docx.xor

---

## License

MIT License

