# Container Sequences: hold reverense to the objects they contain
# Flat Sequences: store value of each item in it's own memory space
# Flat Sequences are more compact, but limited to primitive values

# Mutiple Sequence: Can be changed (list, array, dict)
# Immutable Sequence: Cannot be changed (tuple, bytes, string, int)
# ex. string can be added together to create a new string, 
# you can access substrings, but you can't actually alter the string itself.

# List Comprehension and Readability
# Build a list of Unicode codepoints from a string
symbols = '$¢£¥€₹'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# Same list, different format
code = [ord(symbol) for symbol in symbols]
print(code)

# ord(): an integer representing the Unicode code point of the character when the argument is a unicode object