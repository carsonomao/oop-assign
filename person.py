class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
         print(f"Hello my name is {self.name},I am {self.age} years old ad I'm a {self.gender}.")


def main():
    person = Person("Carson",22,"male")
    person.introduce()

if __name__ == "__main__":
    main()