class person:
    _name = "sudh"
    _surname = "kumar"
    yob = 1990




    def _age(self, current_year):
        return current_year - self.yob
obj = person()
print(obj)



class employee:
    _name = "sudhshanshu"
    __surname = "singh"




obj2 = employee()

print(obj._age(2020))

print(obj2._name)
print(obj2._employee__surname)



