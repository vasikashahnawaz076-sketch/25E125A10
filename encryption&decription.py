name="Vasika"
encrypted = ""
for char in name:
    encrypted += chr(ord(char) + 3)

print(encrypted)

decrypted=""
for c in encrypted:
    decrypted += chr(ord(c) - 3)
print(decrypted)