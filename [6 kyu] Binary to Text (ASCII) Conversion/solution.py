def binary_to_string(binary):
    return ''.join(chr(int(binary[a:a + 8], 2))
                   for a in range(0, len(binary), 8))

print(binary_to_string('00000001'))