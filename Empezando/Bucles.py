#x = 0

#while x <= 10:
#    print(x)
#    x = x+1

for char in "loops":
    print(char)

print("---------------------")

for char in ["I", "LOVE", "PYTHON"]:
    print(char)

print("---------------------")

for number in range(20):
    print(number)

print("---------------------")

for number in range(8,20):
    print(number)

print("---------------------")

for number in range(10,21,2):
    print(number)

# precios de articulos: 5, 10, 15, 20, 25
print("---------------------")
total = 0

for number in [5, 10, 15, 20, 25]:
    total += number
print(f"El total de dolares gastados es: {total}")

print("---------------------")
for a in range(3):
    for b in range(3):
        for c in range(3):
            print(f"{a}, {b}, {c}")