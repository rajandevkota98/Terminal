class ineuron:
    def students(self):
        print("print a students details")

class class_type:
    def students(self):
        print("print class_student")

def ineuron_external(a):
    a.students()

i = ineuron()

j = class_type()

ineuron_external(i)

ineuron_external(j)

