CURRENT_YEAR = 2026

first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
city = input("City: ")

full_name = f"{first_name} {last_name}"

name_length = len(full_name)
born_around = CURRENT_YEAR - age

print("-" * 30)
print(f"{full_name}, {age}")
print(f"{city}")
print(f"Name length: {name_length} characters")
print(f"Born around: {born_around}")
print("-" * 30)