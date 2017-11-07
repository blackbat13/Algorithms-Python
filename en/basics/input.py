print("Reading text from user.")

word = input("Enter one word: ")

print(f"You entered {word}")

print()
print("Reading text from user and parsing it as number.")

word = input("Enter one number: ")
number = int(word)

print(f"You entered {number}. If we add one we will get {number + 1}")
# Please note that operation word + 1 would result in an error, because word is not a number.
# That's why we need to parse it as a integer.


print()
print("Reading text from user and parsing it as number - compact solution.")

number = int(input("Enter one number: "))

print(f"You entered {number}. If we add one we will get {number + 1}")
