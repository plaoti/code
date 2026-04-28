class Animal:
    def __init__(self, name):
        self.name = name
class elephant(Animal):
    def speak(self):
        return f"{self.name} says wooooo..."
my_elephant = elephant(name='끼리')
print(my_elephant.speak())