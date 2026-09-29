s = "([{}])"

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

valid = True

for char in s:

    if char in "([{":
        stack.append(char)

    elif stack and stack[-1] == pairs[char]:
        stack.pop()

    else:
        valid = False
        break

if valid and not stack:
    print("Valid")
else:
    print("Invalid")


