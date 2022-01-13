'''
Created on 
Course work: 
@author: Elakia VM
Source:
    
'''

def startpy():   
    """
    BASIC- I
    """

    # this is for seeing the version
    import sys
    print(sys.version)
    print(sys.version_info)
    """ this is the multi lines comments 
        sys.version shows the version of the python
    """
    """
    Casting 
    If u want to specify the type of a variable
    """
    x = str(3)
    y = int(3)
    z = float(3)
    print(x) #x = '3'
    print(y)
    print(z)

    """
    Get the Type
    show what is the variable 
    """
    print(type(x))
    print(type(y))
    print(type(z))

    """
    Quotes
    variable can be declare in the (" ",' ')
    """
    x = "John"
    print(x)
    x = 'John'
    print(x)

    """
    Case-Sensitive Variable  
    """
    a = 34
    A = "hi"
    print(a)
    print(A)

    # Camel Case
    myVarVal = 34

    #Pascal Case
    MyVarVal = 23

    #Snake Case
    my_var_name = 67

    """
    Many variable accessing
    """
    x,y,z = 3,4,5
    print(x,y,z)

    """
    One value for multiple variables
    """
    x = y = z = 34
    print(x,y,z)

    """
    Unpackage a collection
    """
    a = ['john','raji','sara']
    x, y, z = a
    print(x,y,z)

    """
    Output Variable
    """
    x = "Hello World statement"
    print("Hello " in x)

    y = "printed"
    print(x + y)

    z = 5
    print(x + y + str(z))
    
if __name__ == '__main__':
    startpy()