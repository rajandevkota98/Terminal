class ineuron:
    def __init__(self):
        self.__students = "data science"
        self.std1 = "hello there"

    def student_function(self):
        print(self.__students)
        print(self.std1)


l = ineuron()
l.student_function()
l.__students = "big data"

l.std1 = "new new"

l.student_function()