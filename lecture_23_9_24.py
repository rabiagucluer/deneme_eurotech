######    EXCEPTION HANDLING   ######
# you have to look at first error type and error explanation
# if there are syntax errors first syntax will solve
# if you don't expect another errors let python give you errors


# Exception Handling is a technique in programming that allows a program to respond to and manage errors or exceptional conditions that occur during runtime.
# When a program encounters an error, it could crash or behave unexpectedly.
# Exception handling ensures that such errors are caught and handled gracefully, allowing the program to continue or exit safely.
# try: Contains the code that may cause an error.
# except: If an error occurs in the try block, the except block executes.
# else: If no error occurs in the try block, the else block runs.
# finally: Executes no matter what, whether an exception occurs or not, often used for cleanup.

a=10
b=0
c=a/b

print(f"The result is {c}")
my_dictionary={"isim": "Rabia"}
my_dictionary["yas"]

## try with konusuna bak!!
try:
    print("Code is running")
    c = a / b                   #ZeroDivisionError expected
    print(c)
    print(my_dictionary["yas"]) #KeyError expected
    #print("a"/3)               #TypeError expected
    print("Code is ended")
except ZeroDivisionError as inf:
    print(f"Python will show you this error: {inf}") #bu kisim hatanin nerde oldugunu gösterir
    if b==0:
        print("You need do change b value")
    print("An error has occurred")
except KeyError as inf:
    print(inf)
    print("You got KeyError")
else:                       #if try block is run and any expect blok is not run , else block will run
    print("No error")
finally:                    #even if you have an error you want to run your code. this time this block will run
    print("This block always runs")


#raise error handling

def check_positive(number):
    if number < 0:
        raise ValueError("The number cannot be negative!")
    return number

try:
    check_positive(-5)
except ValueError as e:
    print(f"Error: {e}")



import pandas as pd

df=pd.read_csv("example.txt")

try:
    #print(df)   #NameError expected
    df=pd.read_csv("example.txt")
    print(df)  #FileNotFoundError expected

except NameError :
    print(f"Error: file not found ")

except FileNotFoundError as e:
    print(f"Error: {e}")

finally:
    print("This block always runs")


##### 