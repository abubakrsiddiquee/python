

#Defining a  functions
def bucky():
    print("I'm writing python in VS Code ")
    print("I'm writing python in VS Code ")
    print("I'm writing python in VS Code ")
bucky()


#2

def bucky():
    text ="I'm writing python in VS Code "
    print(text)
    print(text)
    print(text)
bucky()


#3
def bucky(text):
    print(text)
    print(text)
bucky("I'm writing python in VS Code ")

#4

def school_calculator(age):
    if age==5:
        print("Ali can go to school")
    elif age>5:
        print("ALi can go to higher school")
    else:
        print("Ali is a baby")
school_calculator(23)
      

#5
def future_age(age):
    new_age=age+23
    return new_age
    # print(new_age)
predicted_age =future_age(18)
print(predicted_age )
     
    
    