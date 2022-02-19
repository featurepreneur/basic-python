'''
Created on 
Course work: 
@author: Elakia V M
Source:
    
'''

# Import necessary modules
'''
if we print __name__we alway get the __main__ var
'''
print("This is module name file {}".format(__name__))

'''
what is the diff b/t using startpy() way of writing

because when we use this file as module and input then it excutes 
automatically all the funcs at once 
'''
def step1():
    print("prints the step1 func....")

def step2():
    print("prints the step2 func....")

def step3():
    print("prints the step3 func....")

'''
If we use it in the main func to excute then    
'''
# def startpy():
#     print("this statement is alway printed")
#     step1()
#     step2()
#     step3()



if __name__ == '__main__':
#     startpy()

    step1()
    step2()
    step3()

