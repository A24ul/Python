#rect.set_height(8)
#rect.set_width(16)
#(self.width // shape.width) * (self.height // shape.height)
#print(16//2)
#print(16/2)
#print(16%2)
#print(8//4)
import time
start_time = time.time()

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


lst = [1,2,3,3,4,5,4,6]
print(type(lst))
print(lst)
lst_set = set(lst)
print(lst_set)
print(type(lst_set))
print(lst[1])

set_a = {1, 2, 3, 4}
set_b = {2, 3, 4, 5, 6}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.symmetric_difference(set_b))
print(set_a.difference(set_b))


def recursive_countdown(number):
    if number < 1:
        return
    recursive_countdown(number - 1)
    print(number)

recursive_countdown(5)


def change_string(string):
    if string == "":
        return ""
    return change_string(string[1:]) + string[0]

Word = 'ABCDE'
print(Word[1:])
print(Word[0])
print(Word[1:]+Word[0])
print(change_string('ABCDE'))
#print("--- %s seconds ---" % (time.time() - start_time))

#arr = [1,2,3,4,5,6]
#for i in range(1,100000):
#    if i not in arr:
#        arr.append(i)
#    arr.append(i)
#print(arr)

print("--- %s seconds ---" % (time.time() - start_time))

number = 100
print(max(1, number))



lst = [83, 4, 24, 2]
print(lst[:0])
print(lst[0])
print(lst[0+1:])