def collatz_step(n):
    if not n%2:
        return n//2
    return (3*n+1)//2

number = int(input("Give me a number to apply the alg: "))
steps = int(input("Give me the steps desired: "))

count = 0
for i in range(steps):
    print(number)
    if (number & (number - 1)) == 0:
        print("Reached power of 2 in {} steps".format(count))
        break
    number = collatz_step(number)
    count += 1
