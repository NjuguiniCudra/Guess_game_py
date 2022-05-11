import random as r #imported the module/library

num=r.randrange(100)  #range 1..100
Guess = 5  #variable

#condition helps us detects how many chances we are going to have
while Guess>=0:  #condition to get to 0 then stop  
    your_guess=int(input("enter your Guess:"))  #get input from user


    def check(x): #x generates a random number /The value of x depends with the number you input first
        if your_guess == x:
            print('you win')
        elif your_guess > x:
            print("You are close, keep trying lower")
        else:
            print('You are close,keep trying higher')

    if Guess > 1:
        check(num)
    elif Guess == 1:
        check(num)
        print('This is your last chance, make the most of it')
    else:
        print("you lost")
    Guess == Guess - 1  #itarating the value of Guess ...Guess decrementing by negative one and after 0 it comes out of the loop