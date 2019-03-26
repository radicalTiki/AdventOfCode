input = 919901
chars = [int(x) for x in str(input)]

one, two = 0, 1
recipes = [3, 7]
while len(recipes) < input + 10:
    for char in str(recipes[one] + recipes[two]):
        recipes.append(int(char))
    one = (one + 1 + recipes[one]) % len(recipes)
    two = (two + 1 + recipes[two]) % len(recipes)
print("1: %s" % ''.join(map(str, recipes[input:input + 10])))

one, two = 0, 1
recipes = [3, 7]
while recipes[-len(chars):] != chars and recipes[-len(chars) - 1:-1] != chars:
    for char in str(recipes[one] + recipes[two]):
        recipes.append(int(char))
    one = (one + 1 + recipes[one]) % len(recipes)
    two = (two + 1 + recipes[two]) % len(recipes)
if recipes[-len(chars):] == chars:
    print("2: %d" % (len(recipes) - len(chars)))
else:
    print("2: %d" % (len(recipes) - len(chars) - 1))

