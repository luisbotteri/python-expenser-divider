name = input("Hi! Please, write your name: ")
second_name = input("If you have a second name, write it. If not, just press enter: ")
surname = input("Now, please write your surname: ")

if name and surname:
    full_name = f"{name} {second_name + ' ' if second_name else ''}{surname}"
    print(f"Hello, {full_name}, hope you're doing great today!")
else:
    print("Did you write your full name?")
full_name_lenght = len(full_name)
print(f"The quantity of characters that your name has is: {full_name_lenght}!")