import hashlib
def calculate_hash(input_data, hash_type):
    """Calculate hash value for input data."""
    hash_obj = hashlib.new(hash_type)
    
    if isinstance(input_data, str):
        hash_obj.update(input_data.encode('utf-8'))
    elif isinstance(input_data, bytes):
        hash_obj.update(input_data)
    elif isinstance(input_data, (bytearray, memoryview)):
        hash_obj.update(bytes(input_data))
    elif isinstance(input_data, (list, tuple)):
        for item in input_data:
            hash_obj.update(bytes(item))
    else:
        raise ValueError("Unsupported input type")

    return hash_obj.hexdigest()

# Test with the given exercise
text_input = "UIT Cryptography"
hex_input = text_input.encode('utf-8').hex()
file_path = "./context1.txt"  # replace with the actual file path

md5_text_hash = calculate_hash(text_input, 'md5')
sha1_text_hash = calculate_hash(text_input, 'sha1')
sha256_text_hash = calculate_hash(text_input, 'sha256')

md5_hex_hash = calculate_hash(hex_input, 'md5')
sha1_hex_hash = calculate_hash(hex_input, 'sha1')
sha256_hex_hash = calculate_hash(hex_input, 'sha256')

with open(file_path, 'rb') as file:
    file_data = file.read()
    md5_file_hash = calculate_hash(file_data, 'md5')
    sha1_file_hash = calculate_hash(file_data, 'sha1')
    sha256_file_hash = calculate_hash(file_data, 'sha256')
# Print the results with improved formatting
print("Hash Values:")
print(f"Text Input:\n  MD5: {md5_text_hash}\n  SHA-1: {sha1_text_hash}\n  SHA-256: {sha256_text_hash}")
print(f"Hex Input:\n  MD5: {md5_hex_hash}\n  SHA-1: {sha1_hex_hash}\n  SHA-256: {sha256_hex_hash}")
print(f"File Input:\n  MD5: {md5_file_hash}\n  SHA-1: {sha1_file_hash}\n  SHA-256: {sha256_file_hash}")