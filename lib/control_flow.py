#!/usr/bin/env python3

def admin_login(username, password):
    if username =='admin' and password =='12345':
        print("Access granted") 
    else:
        print('Access denied')
def hows_the_weather(temperature):
    if temperature < 40:
        print("Brisk")
    elif 40 <= temperature < 65:  
        print("It's a little chilly out there!")
    elif temperature > 85:
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")


def fizzbuzz(num):
    if num %3==0 and num %5==0 :
        print("Fizzbuzz")
    elif num %3==0 :
        print("Fizz")
    elif num %5==0:
        print("Buzz")

def calculator(operation, num1, num2):
    if operation == '+':
      print(num1+num2)
    elif operation == '-':
      print(num1-num2)
    elif operation == '/':
        print(num1/num2)  
    elif operation == '*' :
        print(num1*num2)


admin_login(username="admin",password=12345)     
hows_the_weather(temperature=25)  
fizzbuzz(15)
calculator(operation="*",num1=15,num2=3) 
    
