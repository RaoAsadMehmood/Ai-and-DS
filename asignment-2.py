# Create a string s containing your full name. Print the string.

full_name = "Saad Naseem"
print(full_name)


# Create a string s with a sentence of your choice and print its length.

sentence = "My name is Saad and I'm persuing bachelors in Fintech from FAST "
length = len(sentence)
print(length)

# Assign a string to a variable and check its data type using Python
word = "toxicity"
data_type = type(word)
print(data_type)

# Create a variable word with the value "Python" and print the first character.
word = "Python"
print(word[0])

# Create a variable course with the value "Python" and print the character at index 3.
course = "Python"
print(course[3])

# Create a variable framework with the value "TensorFlow" and print the character at negative index -4.

framework = "TensorFlow"
print(framework[-4])


# Create a variable fruit with the value "Apple". Convert the string to uppercase and print it.
fruit = "Apple"
upper_text = fruit.upper()
print(upper_text)

# Create a variable city with the value "Karachi". Convert the string to lowercase and print it.
city = "karachi"
lower_case = city.lower()
print(lower_case)

# Create a variable framework with the value "Django". Check if the string starts with "D" and print True or False.

framework = "Django"
if framework[0]=="D":
    print(True)
else:
    print(False)


# Create a variable subject with the value "Mathematics". Check if all characters are alphabetic and print True or False.
subject = "Mathematics"
if subject.isalpha():
    print(True)
else:
    print(False)

# Ask the user to enter their email in any format.and then Convert it into lowercase.

user_email = input("Enter your email in any format");
lower_email = user_email.lower()
print(lower_email)


# check if a number is even or odd where number is taken as input

user_input = int(input("Enter your number"));
if user_input > 0:
    print("Positive")
else:
    print("Negative")