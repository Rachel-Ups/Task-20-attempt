# Modified the program to accept input from the user
name = input("Enter your name: ")

# Now adapted so that only an integer can be entered
age = int(input("Enter your age: "))

# Check the age and print a message accordingly
if age > 50:
    print("Hello,", name + ", you are old at", age, "years.")
else:
    print("Hello,", name + ", you are young at", age, "years.")

