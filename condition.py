'''
Created on 
Course work: 
@author: Elakia V M
Source:
    
'''

# Import necessary modules
 


def startpy(**y):
     for key, value in y.items():
        print(type("%s == %s" % (key, value)))


if __name__ == '__main__':
    startpy(x = "Hello World",	
    a = 20	,
    b = 20.5,	
    c = 1j	,
    d = ["apple", "banana", "cherry"]	,
    e = ("apple", "banana", "cherry")	,
    f = range(6)	,
    g = {"name" : "John", "age" : 36}	,
    h = {"apple", "banana", "cherry"}	,
    i = frozenset({"apple", "banana", "cherry"})	,
    j = True	,
    k = b"Hello",	
    l = bytearray(5)	,
    m = memoryview(bytes(5)) 
)