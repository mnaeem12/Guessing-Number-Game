#--------------------- The Gessing Number Game---------------------------------------------
print('*********Guessing Number Game*********')
import random
#----------------------input range numbers ------------------------------------------------
print("Please Enter two number")
while True:
    try:
        first_number = int(input("Enter The first number  :>"))
        second_number = int(input("Enter The second number :>"))
        if second_number<first_number:
            numbers=range(second_number, first_number)
            break
        elif second_number>first_number:
            numbers=range(first_number, second_number)
            break 
        else:
            print("you must enter defferent numbers")    
    except ValueError:
        print('invalid numbers please enter integer numbers')    
    
length= len(numbers)
#------------------Guessing Function ----------------------------------------------------
def guessing_function(first_numb, second_numb):
    guess_number = random.choice(numbers)
    ges = True
    counter = 0
    print("Guess Number between {0} and {1}" .format(str(first_numb), str(second_numb)))
#-------------------Guess Number from list ----------------------------------------------   
    while ges:
        try:
            player_guess = float(input('Guess Number:>'))
            counter += 1
            if player_guess in numbers:
                print ('in range')
                if player_guess == guess_number:
                    print("Good Right Guessing 👌")
                    ges = False
                    return counter
                elif player_guess > guess_number:  
                      print('your number is high guess less number 👇')
                elif player_guess < guess_number:  
                      print('your number is lower guess high number 👆')
            else:
                print ('Sorry your number out of range please try again')
                ges = True

        except ValueError:
            print('invalid number please try again')
            ges = True

#-----------------Calculating and printing Result--------------------------------------+
count = guessing_function(first_number, second_number)
score = count/length * 100
print("The Number of Attempt is {0} your score is {1}".format(str(count), str(score)))
