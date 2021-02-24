#global variables
x=10
y="hopjesvla"
#at this point no function can be called
#Python does not know that any exists yet

#functions
def change(number):
  number=number*5
  return number

def uppercase(s):
  return s.upper()

z=change(x)
print("x is :",x, "   z is ", z)
str=uppercase(y)
print("y is ", y,"   str is ", str)
