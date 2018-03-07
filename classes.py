class Tard(object):
    def __init__(self, age, height, name, skills):
        self.age = age
        self.height = height
        self.name = name
        self.skills = skills
    def qualified(self):
        if self.age > 16 and self.height > 6:
            self.skills = input(("{} is qualified, but what are his/her skills?   ".format(self.name)))
            print("So your applicants name is {} and he can {}".format(self.name, self.skills))
        else:
            print("Sorry, {} is not qualified.".format(self.name))
def get_info():
    name = input("What is the applicant\'s name?   ")
    age = input("What is {}\'s age?   ".format(name))
    height = input("What is {}\'s height?   ".format(name))
    return(int(age), int(height), name)
info = get_info()
app = Tard(info[0], info[1], info[2], None)
app.qualified()

