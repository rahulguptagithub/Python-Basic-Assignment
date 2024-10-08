SOLUTION 1-

-Python has a clean and readable syntax.
-Runs on various operating systems (Windows, macOS, Linux).
-Suitable for building RESTful APIs and web services.
-Widely used in data science with libraries like Pandas and Matplotlib.
-Libraries like TensorFlow and scikit-learn make it ideal for ML applications.
-frameworks like Django and Flask streamline web application development.

SOLUTION 2-

-Predefined keywords in Python are reserved words  have special meaning in the language. They can't be used as
identifiers like ;- variable names or function names and are integral to Python's syntax and structure. some
key roles they play,  with examples:

-Keywords  if, else, elif, for, while, and break control the flow of execution in a program.
-Keyword  def are use to define functions, while return is used to return values from them.
-keyword class is used to define a new class.
-Keywords like try, except, finally, and raise are used for error handling.
-

-below a simple Python program that demonstrates the use of various keywords:

example:
        
        
def check_even_odd(number):
    
    if number % 2 == 0:
        return True  
    else:
        return False


if __name__ == "__main__":  
    
    for num in range(1, 11):  
        if check_even_odd(num): 
            print(f"{num} is even")  
        else:
            print(f"{num} is odd")


try:
   
    value = int(input("Enter a number: "))  
except ValueError:  
    print("That's not a valid number!")  


SOLUTION 3-

- Mutable objects can be changed in place, meaning their content can be modified without changing their identity.
Examples -

        
my_list = [1, 2, 3]
print("Original List:", my_list)


my_list.append(4)
print("Modified List:", my_list)


my_list[0] = 10
print("After changing first element:", my_list)


-Definition: Immutable objects cannot be changed after they are created. Any modification results in the creation of a new object.
Examples: Tuples, strings, frozensets.

     
my_tuple = (1, 2, 3)
print("Original Tuple:", my_tuple)


new_tuple = my_tuple + (4,)
print("New Tuple after adding an element:", new_tuple)


SOLUTION 4-

-These operators perform basic mathematical operations.

a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b) # Output: 3
print(a % b)  # Output: 1
print(a ** b) # Output: 1000

Comparison Operators:
                     
x = 5
y = 10
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= 5)  # Output: True
print(y <= 10) # Output: True

Logical Operators:
a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False


SOLUTION 5-:
 Implicit Type Casting:

a = 5        
b = 2.5     
result = a + b  
print(result)   
print(type(result))  

 Explicit Type Casting:

a = 5.7
b = int(a)
print(b) 
x = 10
y = float(x)
print(y)  
s = "123"
num = int(s)
print(num) 


n = 456
str_num = str(n)
print(str_num) 

SOLUTION 6-
 Conditional statements in Python allow you to execute code based on specific conditions.
These are mainly achieved using if, elif, and else statements. The condition is typically
an expression that evaluates to either True or False.

example 1- 
x = 10
if x > 5:
    print("x is greater than 5")
# Output: x is greater than 5
 example 2-
x = 3
if x > 5:
    print("x is greater than 5")
elif x == 3:
    print("x is equal to 3")
# Output: x is equal to 3

example 3-
x = 7
if x > 5:
    print("x is greater than 5")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
# Output: x is greater than 5
#         x is odd



SOLUTION 7-
Python provides two primary types of loops: the for loop and the while loop. 
Each serves different use cases, depending on whether you know the number of
iterations in advance or need to loop based on a condition.

example- 
for loop-
for variable in sequence:
    # Code block to execute


Iterating through a list:
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
 

 while Loop:
    while condition:
    # Code block to execute
 
 else with Loops:
for i in range(5):
    print(i)
else:
    print("Loop completed without break.")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed without break.



