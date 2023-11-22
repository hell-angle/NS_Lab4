import hashlib

def count_differing_bytes(message1, message2):
    """Count the number of differing bytes between two messages."""
    differing_bytes = sum(b1 != b2 for b1, b2 in zip(message1, message2))
    return differing_bytes

def generate_md5_hash(message):
    """Generate the MD5 hash value for a message."""
    md5_hash = hashlib.md5(message).hexdigest()
    return md5_hash

# Messages in hexadecimal format
hex_message1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89" \
                "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8" \
                "823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f" \
                "33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"

hex_message2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8" \
                "955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd728037" \
                "3c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d" \
                "248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965a" \
                "b6ff72a70"

# Convert hex strings to bytes
message1 = bytes.fromhex(hex_message1)
message2 = bytes.fromhex(hex_message2)

# Count differing bytes
differing_bytes_count = count_differing_bytes(message1, message2)

# Generate MD5 hash values
md5_hash1 = generate_md5_hash(message1)
md5_hash2 = generate_md5_hash(message2)

# Print results
print(f"Number of differing bytes between messages: {differing_bytes_count}")
print(f"MD5 Hash of Message 1: {md5_hash1}")
print(f"MD5 Hash of Message 2: {md5_hash2}")
