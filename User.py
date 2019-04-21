from BaseUser import BaseUser


class User(BaseUser):
    def __init__(self, name, age, identifier):
        BaseUser.__init__(self, identifier)
        self.name = name
        self.age = age

    def info(self):
        print("name: " + self.name + ", age: " + str(self.age) + ", id: " + self.identifier)
