#this is a timed math quiz

import random #random because we will randomly generate operators
import time #we need to see the time for our quiz
OPERATORS = ["+", "-", "*"] # all our operators
MIN_OPERAND = 3 #min number we want to work with
MAX_OPERAND = 12 #max number we want to work with
TOTAL_PROBLEMS = 10 #this is the max amount of problems we will have

def generate_problems():#we will make random equations
    left = random.randint(MIN_OPERAND, MAX_OPERAND) #this will take a random number between 3 and 12
    right = random.randint(MIN_OPERAND, MAX_OPERAND) # this will take a random number between 3 and 12
    operator = random.choice(OPERATORS)#randomly picks something from our OPERATORS
    expression = str(left) + " " + operator + " " + str(right) # our expression is created right here make the integer into a string
    answer = eval(expression) # then python can check what the answer is to see if we got it right
    return expression, answer

wrong= 0 #basically we set this 0 because then we can have python keep asking us the same question if we get it wrong
input("Press enter to start!")
print("---------------------")

start_time = time.time() # this is to start the timer for the quiz

for i in range(TOTAL_PROBLEMS): # so this will make our 
    expression, answer = generate_problems() #right here it makes us a UNIQUE problem
    while True:
        guess = input("Problem #" + str(i+1)+ ": " + expression + "= ") #this is just for telling us what problem we on
        if guess == str(answer): #answer will be an integer guess will be a string so we need both as string if you do guess to int then it will crash the string
            break#break right here because if its right then we don't have to keep reasking the question
        wrong += 1

end_time = time.time()#once you are done then it gets the end time
total_time = round(end_time - start_time, 2) # this will get your total time and also round it 2 spots.


print("---------------------")
print("Nice Work! You finished in", total_time, "seconds!")







