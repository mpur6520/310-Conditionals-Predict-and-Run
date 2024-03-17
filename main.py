#Maru Puran
#October 24 2023
#analyze predict and run code containing else if else and if statements as well as variables to garner an understanding of how code containing conditionals works


# Example code 1

#this overall code has the user input a guess to a number between 1 and 10 and alerts then if their guess is too high, too low, or if it's right

number = 7 #set number variable equal to numerical value 7
print("I have thought of a number between 1 and 10") #print this message telling the user that it's thinking of a number between 1 and 10 (7 assigned to number)
guess = int(input("Can you guess what it is?")) #asks user to guess the number between 1 and 10, stores number numerically as an integer in the variable created called guess

if guess == number: #checks if the guess and number is equal to each other; if the guess = 7
  print("Correct!") #print the following message to alert the user that they're correct
elif guess < number: #check the user if the guess is less than the number; if guess < 7 if previous condition isn't met
  print("Too Low!") #print the following message to alert the user that their guess is too low
else: #runs if all statements are false, indicating the guess is too high
  print("Too High!") #print the statement that the guess the user inputted is too high

#the user doesn't have to enter a number between 1 and 10, the program will run anyway. In order to alert the user their answer is invalid there would have to be code checking if the guess is greater than 10 or less than 1.

#if the user enters something using letters like "two" instead or "2", there will be an error (value error)

# Example code 2


#the overall code has the user input two numbers and compares the two, allowing the user to know if one is greater than, or if the numbers are equivalent

number1 = int(input("Please enter a number")) #ask the user to enter a number as an integer and save it in the variable number1 as an integer
number2 = int(input("Please enter another number")) #ask the user to enter a number as an integerand save it in the variable number2 as an integer

if number1 > number2: #checks if number1 inputted is greater than number2
  print("Number 1 is bigger than number 2") #if this is true then alert the user number1 is greater than number2 with the message inside quotations
elif number2 > number1: #if false, then check if number2 is equal to number1
  print("Number 2 is bigger than number 1") #if this conditional is true then print the following code alerting the user number2 is greater than number1, only runs if conditional previous isn't true
else: #if both statements are false this means the numbers are the same
  print("Both numbers are the same") #alert the user that the numbers are the same by printing the message in quotations

#if the user enters something using letters like "two" instead or "2", there will be an error (value error)