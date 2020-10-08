n = int(input('Enter number: '))
m = n % 10
z = m % 10
while m > z:
    z = z % 10
print(m)