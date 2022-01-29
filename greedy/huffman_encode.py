def get_huffman_code(s):
    d = []
    for i in set(s):
        d.append((i, s.count(i)))
    d.sort(key=lambda x: x[1], reverse=True)
    code = {}
    i = 0
    for letter in d:
        code[letter[0]] = i*'1' + '0'
        i += 1
    if len(d) > 1:
        code[letter[0]] = code[letter[0]][:-1]
    return code

def huffman_encode(s, code):
    encoded = ""
    for symbol in string:
        encoded += code[symbol]
    return encodedd


string = list(input())
code = get_huffman_code(string)

encoded_string = huffman_encode(string, code)

print(len(code), len(encoded_string))
for letter in sorted(set(string)):
    print(f"{letter}: {code[letter]}")
print(encoded_string)