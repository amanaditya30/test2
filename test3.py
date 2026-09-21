n = 7

if n < 2:
    print("Not Prime")

for i in range(2, n):
    if n % i == 0:
        print("Prime")
        break
else:
    print("Not Prime")
