import logging
def printhello():
    print("hello")
logging.basicConfig(filename="logger.log", level=logging.INFO, format='%(asctime)s %(name)s  %(levelname)s %(message)s')
# """"""#Questions
# l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
# 1 . Try to reverse a list
# 2. try to access 234 out of this list
# 3 . try to access 456
# 4 . Try to extract only a list collection form list l
# 5 . Try to extract "sudh"
# 6 . Try to list all the key in dict element avaible in list
# 7 . Try to extract all the value element form dict available in l"""


class String:
    def __init__(self, li):
        self.li = li
    def reverse_list(self):
        """Reversing list"""
        try:
            dict1 = self.li[::-1]
            logging.info("reversed order {}".format(dict1))
        except Exception as e:
            logging.exception(e)
    def find_value(self,x):
        """finding value in list"""
        try:
            for i in self.li:
                if type(i) == int:
                    if i == x:
                        logging.info('{}is present um'.format(x))
                if type(i)==list:
                    for j in i:
                        if j == x:
                            logging.info('{}is present um'.format(x))
                if type(i)== dict:
                    for j in i:
                        if j == x:
                            logging.info('{}is present '.format(x))
                if type(i) == tuple:
                    for j in i:
                        if i == x:
                            logging.info('{}is present '.format(x))
        except Exception as e:
            logging.exception(e)
    def only_list(self):
        """Extracting only list"""
        try:
            list2 = []
            for i in self.li:

                if type(i)== list:
                    list2.append(i)
                if type(i) == dict:
                    for j in i:
                        if type(i) == list:
                            list2.append(i)
                        if type(i[j])== list:
                            list2.append(i[j])
            logging.info("The collections of the list are {}".format(list2))
        except Exception as e:
            logging.exception(e)

    def extract_key(self):
        """extracting only key value"""
        try:
            list3 = []
            for i in self.li:
                if type(i) == dict:
                    for j in i:
                        list3.append(j)
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j)== dict:
                            for k in j:
                                list3.append(k)
            logging.info(list3)
        except Exception as e:
            logging.exception(e)

    def extract_value(self):
        """extracting only value"""
        try:
            list3 = []
            for i in self.li:
                if type(i) == dict:
                    for j in i:
                        list3.append(i[j])
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j)== dict:
                            for k in j:
                                list3.append(j[k])
            logging.info(list3)
        except Exception as e:
            logging.exception(e)


l = [3,4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
     {"key1": "sudh", 234: [23,234, 45, 656]}]
p= String(l)

q= String.reverse_list(p)

r = String.find_value(p,234)
s= String.find_value(p,456)
t = String.only_list(p)
u = String.extract_key(p)
r = String.extract_value(p)

