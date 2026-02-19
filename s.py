# buggy_code.py

def add_numbers(a, b):
    # Missing colon and indentation error
result = a + b
return result

def greet(name):
    print("Hello, " + name)  # Variable name typo

for i in range(5):
    print(i)  # Missing indentation

my_list = [1, 2, 3]
print(my_list[2])  # IndexError: out of range

print("This line is fine")