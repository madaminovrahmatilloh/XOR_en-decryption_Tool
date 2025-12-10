# Smart XOR Encryption & Decryption Tool
# Works on Windows, Linux, and WSL

import os

def xor_bytes(data, key):
    """Encrypt or decrypt bytes using a multi-character key."""
    key_len = len(key)
    return bytes([b ^ ord(key[i % key_len]) for i, b in enumerate(data)])

# --- Text Mode ---
def encrypt_text():
    text = input("Enter text to encrypt: ")
    key = input("Enter key: ")
    if not key:
        print("Key cannot be empty!")
        return
    encrypted_bytes = xor_bytes(text.encode('utf-8'), key)
    encrypted_hex = encrypted_bytes.hex()
    print("Encrypted text (hex):", encrypted_hex)

def decrypt_text():
    hex_text = input("Enter hex text to decrypt: ")
    key = input("Enter key: ")
    if not key:
        print("Key cannot be empty!")
        return
    try:
        encrypted_bytes = bytes.fromhex(hex_text)
    except ValueError:
        print("Invalid hex input!")
        return
    decrypted_bytes = xor_bytes(encrypted_bytes, key)
    try:
        decrypted_text = decrypted_bytes.decode('utf-8')
    except UnicodeDecodeError:
        print("Decryption failed. Check your key or input.")
        return
    print("Decrypted text:", decrypted_text)

# --- File Mode ---
def process_file():
    print("\nEnter the full file path. On Windows paths in WSL, use /mnt/c/... style.")
    filepath = input("File path: ").strip()

    # Remove quotes if present
    if filepath.startswith('"') and filepath.endswith('"'):
        filepath = filepath[1:-1]

    # Replace backslashes with forward slashes for Windows paths
    filepath = filepath.replace("\\", "/")

    # Check if file exists
    if not os.path.isfile(filepath):
        print(f"File not found! Path interpreted as:\n{filepath}")
        return

    key = input("Enter key: ").strip()
    if not key:
        print("Key cannot be empty!")
        return

    with open(filepath, 'rb') as f:
        data = f.read()

    result = xor_bytes(data, key)

    dir_name, filename = os.path.split(filepath)

    if filename.endswith(".xor"):
        out_filename = filename.replace(".xor", "_decrypted")
        action = "decrypted"
    else:
        out_filename = filename + ".xor"
        action = "encrypted"

    out_path = os.path.join(dir_name, out_filename)

    with open(out_path, 'wb') as f:
        f.write(result)

    print(f"File {action} successfully: {out_path}")

# --- Main Menu ---
def main():
    while True:
        print("\n=== Smart XOR Encryption & Decryption Tool ===")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Encrypt/Decrypt File")
        print("4. Exit")

        choice = input("Choose option (1/2/3/4): ").strip()

        if choice == '1':
            encrypt_text()
        elif choice == '2':
            decrypt_text()
        elif choice == '3':
            process_file()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
