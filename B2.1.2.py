import hashlib

def calculate_hashes(file_path):
    # Initialize hash objects for MD5, SHA-1, and SHA-256
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()

    # Open the file in binary mode and read it in chunks
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(4096)  # Read in 4KB chunks
            if not chunk:
                break
            md5_hash.update(chunk)
            sha1_hash.update(chunk)
            sha256_hash.update(chunk)

    # Get the hexadecimal representations of the hash values
    md5_digest = md5_hash.hexdigest()
    sha1_digest = sha1_hash.hexdigest()
    sha256_digest = sha256_hash.hexdigest()

    return {
        "MD5": md5_digest,
        "SHA-1": sha1_digest,
        "SHA-256": sha256_digest
    }

if __name__ == "__main__":
    file_path1 = r"D:\NS\Lab4\md5-1.docx"  # Replace with the path to the first .exe file
    file_path2 = r"D:\NS\Lab4\md5-1fc.jpg"  # Replace with the path to the second .exe file
    hash_values1 = calculate_hashes(file_path1)
    hash_values2 = calculate_hashes(file_path2)

    print("Hash values for erase.exe 1:")
    print("MD5:", hash_values1["MD5"])
    print("SHA-1:", hash_values1["SHA-1"])
    print("SHA-256:", hash_values1["SHA-256"])

    print("\nHash values for hello.exe 2:")
    print("MD5:", hash_values2["MD5"])
    print("SHA-1:", hash_values2["SHA-1"])
    print("SHA-256:", hash_values2["SHA-256"])
