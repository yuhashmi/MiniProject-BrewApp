a = {}

b = int(input("Number of elements: "))

for i in range(b):
    k = input("Enter key: ")
    v = input("Enter value: ")
    a.update({k:v})

print(a)