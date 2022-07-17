class Person:
    def __init__(self, name, surname, dob):
        self._name = name
        self.__surname = surname
        self.dob = dob

    def return1(self):
        print(self._name, self.__surname)
raj = Person('Rajan ', ' Devkota', 2058)

# print(raj._name)
# print(raj.__surname)
  # -- means private
raj.return1()



#whenever you have to access private value
print(raj._Person__surname)