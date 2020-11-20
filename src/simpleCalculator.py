# program make a simple calculator

# this function add two functions

def add(x,y):
    return x+y
# this function substract two numbers
def substract(x,y):
    return x-y
# this function multiplies two numbers
def multiply(x,y):
    return x*y
# this function divides two numbers
def divide(x,y):
    return x/y

x = 11
y = 10
if (x>y):
    print("Hello")
else:
    print("hi")
print("done")

def prime(num):
    if num > 1:
        #check for factors
        for i in range(2,num):
            if (num % 2) ==0:
                return False
            else:
                return True

            # if input number is less than or equal 1, then it is not a prime number
    else:
        return False

# I wrote a small snippet in Python.
# Here you go
l = ["eat", "drink", "sleep"]
def repeat():
    for i in range(len(l)):
        print(l[i])
while True:
    repeat()
