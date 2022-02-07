# Stepic task:
# https://stepik.org/lesson/13239/step/5?unit=3425
#
# По данной непустой строке s длины не более 10^4, 
# состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код. 
# В первой строке выведите количество различных букв k, встречающихся в строке, 
# и размер получившейся закодированной строки. 
# В следующих k строках запишите коды букв в формате "letter: code". 
# В последней строке выведите закодированную строку.
#


import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")
    
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def get_huffman_code(s):
    
    h = []
    for letter in set(s):
        h.append((s.count(letter), len(h), Leaf(letter)))
    heapq.heapify(h)
    
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1+freq2, count, Node(left, right)))
        count += 1
    
    [(_freq, _count, root)] = h
    code = {}
    root.walk(code,"")

    return code

def huffman_encode(s, code):
    encoded = ""
    for symbol in string:
        encoded += code[symbol]
    return encoded


string = list(input())
code = get_huffman_code(string)

encoded_string = huffman_encode(string, code)

print(len(code), len(encoded_string))
for letter in sorted(set(string)):
    print(f"{letter}: {code[letter]}")
print(encoded_string)
