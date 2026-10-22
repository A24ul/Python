print('Hello World')
developer = ['Alice', 25, ['Python', 'Rust', 'C++', 'Java']]
for i in range(len(developer)):
    print("Normal list items: ", [i], developer[i])
    if isinstance(developer[i], list):
        for j in range(len(developer[i])):
            print("Nested list items: ",[i],[j] , developer[i][j])
#    print(type(developer[i]))

#print("Removed 3rd item: " ,developer.pop(2))
#print(developer.index("Alice"))
ABC = 'Alice'
#print(list(ABC))
#print(tuple(ABC))

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Tom':
        break
#print(enumerate(developer_names))


developer_tuple = ('Jane Doe', 23, 'Python Developer')
#del developer_tuple[1]

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
#print(programming_languages.index('Python', 3))


import dictionary

print(__name__)