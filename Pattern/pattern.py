num = int(input("Enter the range: \t "))

for p in range(num):
    print(' '*(num-p-1)+'* '*(p+1))

# reverse pyramid
for rp in range(num-1, 0, -1):
    print(' '*(num-rp)+'* '*rp)
