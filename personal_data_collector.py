print("Welcome to the Interactive Personal Data Collector!")
print("This program collects some basic information from you.\n")

name = input("Please enter your name: ")

age = int(input("Please enter your age: "))
print("Age converted to integer.")

height = float(input("Please enter your height in meters: "))
print("Height converted to float.")

favourite_number = int(input("Please enter your favourite number: "))
print("Favourite number converted to integer.")

# Calculate birth year
year = datetime.now().year
birth_year = year - age

print("\nThank you! Here is the information we collected:\n")

print("Name:", name)
print("Type:", type(name))
print("Memory Address:", id(name))

print("\nAge:", age)
print("Type:", type(age))
print("Memory Address:", id(age))

print("\nHeight:", height)
print("Type:", type(height))
print("Memory Address:", id(height))

print("\nFavourite Number:", favourite_number)
print("Type:", type(favourite_number))
print("Memory Address:", id(favourite_number))

print("\nYour birth year is approximately:", birth_year)
print("This is calculated based on your age of", age)

print("\nThank you for using the Personal Data Collector.")
print("Goodbye!")
