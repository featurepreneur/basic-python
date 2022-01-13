'''
Created on 
Course work: 
@author: Elakia VM
Source:
    
'''

"""
Creating the function
"""
def func():
    print("hello world")

"""
Calling the a function
"""
def func():
    print("this is function calling program")

func()

"""
Arguments
"""
def value(text):
    print("name " + text)

value("ram")
value("raji")
value("sara")

"""
Using **kwargs
"""
def value(**val):
    print("name " + val["lname"])

value(fname = "harini",lname = "sara")

"""
Using the key & value programming 
"""
def vp_fun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
vp_fun(first='hello', mid='world', last='python')

"""
declarartion of global variable
"""
x = "Easy"
def myfun():
    print("python is " + x)

myfun()

"""
Using global Keyword
"""
def met():
    global y
    y = "awersome"

met()
print("Python is " + y)

"""
Passing a list as argu
"""
def list_func(food):
    for x in food:
        print(x)

eat = ["chicken biryani","shawarma","chicken 65"]
list_func(eat)

"""
Return Values
"""
def val_func(x):
    return(25 * x)

print(val_func(4))
print(val_func(6))

"""
pass statement just the function to define 
with any error 
"""
def df_func():
    pass

"""
Recursion function
"""
def rec_func(k):
    if(k<10):
        result = k +rec_func(k+1)
        print(k)
    else:
        result = 0

    return result

print("Recursion Example Result")
rec_func(0)
