from collections import OrderedDict
class funString():

    def __init__(self,string = ""):

        self.string = string

    def __str__(self):

        return self.string

    def size(self) :

        return len(self.string)

    def changeSize(self):

        return self.string.swapcase()

    def reverse(self):

        return self.string[::-1]

    def deleteSame(self):

        return ''.join(OrderedDict.fromkeys(self.string))

         
str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())