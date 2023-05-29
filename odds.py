a = int(input("a: "))
b = int(input("b: "))

if a % 2 == 1:
    c = a
else:
    c = a + 1

for i in range(a + 2, b + 1):
    if i % 2 == 1:
        c = c + i
    else:
        next
    
print(c)
