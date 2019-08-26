#Fizzbuzz, multiple of 3 = Fizz, multiple of 5 = Buzz, multiple of both =  Fizzbuzz

choice = input("Please enter 1 or 2, choice 1 will output from 1 to 100 with fizzbuzz application, choice 2 allows you to enter your own choice of number ")


if choice == 1:
    i = 0
    while i < 100:
        i = i+1
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i  % 3 != 0 and i % 5 ==0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        else:
            print i
if choice == 2:
    while True:
        z = int(input("Please enter a number- to end the program enter z "))
        if z == -1:
            break
        elif (z % 3 == 0) and (z % 5 ==0):
            print("Your number is a multiple of 3 and 5 FizzBuzz!")
        elif (z % 3 == 0) and (z % 5 != 0):
            print("Your number is a multiple of 3 Fizz!")
        elif  (z % 3 != 0) and (z % 5 ==0):
            print("Your number  is a multiple of 5 Buzz!")
        else:
            print("Your number is not a multiple of 3 or 5")
