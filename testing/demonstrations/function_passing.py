

def applier(addFunction, num):
    return addFunction(num)

def sum5(num):
    return 5 + num

def min5(num):
    return 5 - num

class Friend:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def print(self):
        print(f"{self.name} is {self.age} years old and works as a {self.job}")

friendCollab = [
    Friend("Thomas", 93, "Unemployed"),
    Friend("Thanh", 94, "Tram's brother"),
    Friend("Jack", 95, "Barback")
]

friendCollab.sort(key=lambda friend: friend.job)

for friend in friendCollab:
    friend.print()

print("hi")
