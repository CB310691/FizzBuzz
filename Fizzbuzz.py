#Fizzbuzz, multiple of 3 = Fizz, multiple of 5 = Buzz, multiple of both =  Fizzbuzz

choice = input("Please enter 1 or 2, choice 1 will output from 1 to 100 with fizzbuzz application, choice 2 allows you to enter your own choice of number ")
#gives the user a choice of options

if choice == 1:
    i = 0
    while i < 100:
        i = i+1 #iterates through 1->100 and will print every digit and if that number is a multiple of 3, 5, both or neither.
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i  % 3 != 0 and i % 5 ==0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        else:
            print i
if choice == 2: #choice 2 allows the user to input any number they want and the program will tell the user if that number is a multiple of 3, 5, both or neither.
    while True:
        z = int(input("Please enter a number- to end the program enter -1 "))
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
