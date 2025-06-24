import hashlib

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

file_path = input("Enter the path of the file to check integrity: ")
original_hash = input("Enter the original hash value: ")

new_hash = get_file_hash(file_path)
print("Calculated Hash:", new_hash)

if new_hash == original_hash:
    print("✅ File is intact.")
else:
    print("❌ File has been modified!")
