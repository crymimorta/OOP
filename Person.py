class person:
    def __init__(self, name, surname, age=None, gender = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def walk(self):
        print('Person', self.name, ' is walking')

    def info(self):
        print('Person name is ', self.name, ',surname ', self.surname, ',', self.age, 'years old and gender is ', self.gender)