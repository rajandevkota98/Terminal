class Person:
    def __init__(self, name, surname, email, dob):
        self.name = name
        self.surname = surname
        self.email = email
        self.dob = dob


    def age(self, current_year):
        self.current_year = current_year
        return current_year - self.dob

    def ask_dob(self):
        dob = input("Enter the date of birth")
        print(dob)
        return dob



ram = Person('r','2','2','4')

print(ram.name)
print(ram.email)

print(len(ram.name))



class Narayan:
    def __init__ (a, name, roll):
        a.name = name
        a.roll = roll


hello = Narayan('Narau',12)
print(hello.name)



hari = Person('Hari','1','2', 2000)
print(hari.dob)
hari.ask_dob()

print(hari.age(2020))



# Task1- in past whatever qsn have i have given to you with respect to list, tuple , dic, set , string,,, try to create separe class
# for  each and every clas and restructure your code for all the segment and submit.None
#
# instruction number-1
# always use exception handling
#
# instruction number-2
# use logging as well
#
#  reformat your code and submit it to me before tomorrow's class 3pm IST to my mail id
#
# sudhanshu@ineuron.ai

# I am only looking for your separate python file in your github link