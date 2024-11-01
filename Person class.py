# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name  # Attribute for the person's name
        self.age = age    # Attribute for the person's age
        self.gender = gender  # Attribute for the person's gender

    def introduce(self):
        # Method to print the introduction message
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alice", 30, "Female")

# Call the introduce method to display the person's information
person1.introduce()
