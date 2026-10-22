#rect.set_height(8)
#rect.set_width(16)
#(self.width // shape.width) * (self.height // shape.height)
#print(16//2)
#print(16/2)
#print(16%2)
#print(8//4)


string = 'ABCD'
reverse_string = ''
length = len(string)
for i in range(len(string)-1, -1, -1):
    reverse_string += ''.join(string[i])
print(reverse_string)
strg = reversed(reverse_string)
print(strg)

reversed_text = ""
for char in string:
#    print(char)
    reversed_text = char + reversed_text
    print(reversed_text)
print(reversed_text)
print(string)
print(list(string))