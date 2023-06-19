def mapper(test):
    if mapping := [mappings[c] for c in mappings.keys() if c(test) == 0]:
        return mapping
    return [str(test)]

mappings = {(lambda x: x%3):"Fizz", (lambda x: x%5):"Buzz", (lambda x: x%7):"Duck"}

number = int(input("Max number: "))

count = 0
for i in ["".join(mapper(i)) for i in range(1, number)]:
    count += 1
    print(i, end = " ")
    if count % 25 == 0:
        print("\n", end = "")