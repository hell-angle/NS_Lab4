message1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89" \
           "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8" \
           "823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f" \
           "33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"

message2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8" \
           "955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd728037" \
           "3c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d" \
           "248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965a" \
           "b6ff72a70"

# Convert hexadecimal strings to binary
message1_bin = bin(int(message1, 16))[2:]
message2_bin = bin(int(message2, 16))[2:]

# Ensure both binary strings have the same length by padding with zeros if necessary
max_length = max(len(message1_bin), len(message2_bin))
message1_bin = message1_bin.zfill(max_length)
message2_bin = message2_bin.zfill(max_length)

# Count differing bits
differing_bits = sum(bit1 != bit2 for bit1, bit2 in zip(message1_bin, message2_bin))

# Calculate the number of differing bytes
differing_bytes = differing_bits // 8

print(f"The number of differing bytes between the two messages is: {differing_bytes}")
