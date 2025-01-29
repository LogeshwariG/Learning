#Day1

#Print - to print the statement 
#input - using to get a input from the user
#variable declaration - storing a value inside a variable
#variable naming - naming should be proper, should not start with number, while calling the variable name should be without spelling mistake.  
#len function useing to get the length of the value.

#Day 2

# data types
#string = represent within the double codes "Hello"
#integer = represent as numbers print(123)
#float = represent point values 1.345
#Boolean = true, false

#Mathematical operation
# + = Addition
# - = Subtraction
# * = Multiplication
# / = divition , always give you the answer in float data type.
# ** = raising power eg(2 ** 3) 2 power 3 answer will be 8.
# Order = PEMDASLR (Parentheses (), Exponents **, Multiplication *, Divition /, Addition +, Subtraction -, Left to Right)Calculation will go Left to Right


#Day 3

#Conditional Operators
# > Greater than
# < Less then
# >= Greater than or equal to
# <= less than or equal to
# == Equal to
# != Not equal to

# if condition - one condition

# if <condition>:
#    <do this>
# else:
#    <do this>
#example 
#find odd or even

#which number want to check
number = int(input())

#if the number can be divided by 2 with 0 reminder
if number % 2 == 0:
    print("This is even number")

#otherwise number can't be divided with 0 reminder
else:
    print("This is odd number")


# Nested if statement - if condition inside if condition

# if <condition>:
#   if <condition>:
#       <do this>
#   else:
#       <do this>
# else:
#   <do this>    

#example
# fix price if the person hight is above 120cm & age is above 18 then $12,  only hight is above and age is less than 18 then $7.

print("Welcome to roller coaster!!! ")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("you are eligle to ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("your not eligible to ride rollercoaster")


#Find Leap year
'''

This is how you work out whether if a particular year is a leap year.

on every year that is divisible by 4 with no remainder

except every year that is evenly divisible by 100 with no remainder

unless the year is also divisible by 400 with no remainder

If english is not your first language or if the above logic is confusing, try using this flow chart .

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, including spelling an punctuation.

Example Input 1
2400
Example Output 1
Leap year

'''

# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"Leap year")
    else:
      print(f"Not leap year")
  else:
    print(f"leap year")
else:
  print(f"Not leap year")



# if / elif /else - if more than one condition

# if condition1:
#   <do A>
# elif condition2:
#   <do B>
# else:
#   <do this>

#example 
#in the same above concent adding one more condition if the age is less than 12 then pay $5. 

print("Welcome to roller coaster!!! ")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("you are eligle to ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("your not eligible to ride rollercoaster")




#Practice: Find BMI 
#clue BMI = weight / height m^2

#example height = 1.50 , weight = 63 , BMI = 63+(1.50* 1.50) = 28

#BMI is over 18.5 and below 25 = normal 
#BMI is over 25 and below 30 = slightly over weight
#BMI is over 30 and below 35 = obese
#BMI is over 35 = clinically obese

#enter your height in meters
height = float(input())

#enter your weight in Kilograms
weight = int(input())

BMI = weight + (height * height)

if BMI < 25:
    print("Your BMI is {BMI},you are underweight")
elif BMI >= 25 or BMI < 30:
    print("Your BMI is {BMI},you have a normal weight")
elif BMI >= 30 or BMI < 35:
    print("Your BMI is {BMI},you are obese")
else:
    print("Your BMI is {BMI},you are Clinically obese")

#multiple if - all the functions will be executed if the condition is true.

#if condition1:
#   <do A>
# if condition2:
#   <do B>
# if condition3:
#   <do C>
# 

#example 
#in the same above concent adding one more condition if the age is less than 12 then pay $5. and if they want photo adding 3 more dollers

print("Welcome to roller coaster!!! ")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo_required = input("Do you want a photo taken? Y or N")
    if photo_required == "Y" :
        #add 3 dollers
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("sorry, your not eligible to ride rollercoaster")


#escersise:
# find the rate of pizza 

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2 
  else:
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is : ${bill}")


#if condition 
# if condition1 & condition 2 & condition 3:
#   <do this>
# else
#   <do this>


#logical operations
# A and B
# C Or D
# not E

#example 
#in the same above concent adding one more condition if the age is less than 12 then pay $5. and if they want photo adding 3 more dollers. if the age is above 45 - 55 then ticket is free

print("Welcome to roller coaster!!! ")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
       bill = 0 
       print("Free ride for elders")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo_required = input("Do you want a photo taken? Y or N")
    if photo_required == "Y" :
        #add 3 dollers
        bill += 3
    print(f"Your final bill is {bill}")

else:
    print("sorry, your not eligible to ride rollercoaster")

'''
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:
lower() count()

Example Input 1
Kanye West
Kim Kardashian
Example Output 1
The Love Calculator is calculating your score...
Your score is 42, you are alright together.

'''


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine_names = name1 + name2
names_lower = combine_names.lower()
t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")
first_digit = t + r + u + e

l = names_lower.count("l")
o = names_lower.count("o")
v = names_lower.count("v")
e = names_lower.count("e")

second_digit = l + o + v + e

score =int( str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  

#Day 4

#Random module

import random

random_integer = random.randint(1,10)
print(random_integer)


#example exercise
'''
ou are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

Example Output
Heads
or

Tails
'''

import random

number = random.randint(0,1)
if number == 0:
  print("Tails")
else:
  print("Heads")

#List 
#examples of list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


#list order - [0,1,2,3....]

#replacing an item in list - it will replace second item in the list 
states_of_america[1] = "Pencilvania" 

#adding new item in list 
states_of_america.append("Newitemname")

#adding new items more than 1
states_of_america.extend(["newitemone","newitemtwo"])

print(states_of_america)

#exercise 14 
#picking a random person from the list

names = ["Loge", "pavi", "sangee","Manju"]

import random

name = random.choice(names)

print(f"{name} is going to buy the meal today!")


#Nested List - list inside list


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]

vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]
 

dirty_dozen = [fruits , vegetables]
#direty_dozen is the list which had lists

print(dirty_dozen)

friends = ["mani" , "pavi" ,"Manju" ,"sangee" ,"loge" , "kala"]

print(random.choice(friends))




#excercise 15 
'''
This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:

first, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️',

'''


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc =["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")


#Day 5
#For loop with lists

fruits = ["Apples", "Peaches", "Pears"]

for fruit in fruits:
   print(fruit) #in loop
   print(fruit + "pie") #in loop
print(fruits) # will print after for loop ends 

#fine the max value in the student_scores list with out using direct max() function


student_scores = [180, 124, 165, 173, 189, 169, 146]
max = 0
for score in student_scores:
   if score > max:
    max = score
print(max)
   
#For loops and range() function

total = 0

for number in range(1, 101):
   total += number
print(total)


#Exercise : 6
'''
Coding Excercise FizzBuzz

You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:



Your program should print each number from 1 to 100 in turn and include number 100.



But when the number is divisible by 3 then instead of printing the number it should print "Fizz".



When the number is divisible by 5, then instead of printing the number it should print "Buzz".`



And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

'''

#solution:

for number in range(1, 16):
    if (number % 3) == 0 and (number % 5) == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# password generator

import random
import numpy as np

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')','+']

print("Welcome to password generator")

num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password?"))
num_symbols = int(input("How many symbols would you like in your password?"))

random_letters = random.sample(letters ,num_letters )
random_numbers = random.sample(numbers,num_numbers)
random_symbols = random.sample(symbols,k = num_symbols)


result = random_letters + random_numbers + random_symbols


final_result = ''.join(result)

print(final_result) # without shuffling the random letters, numbers, symbols

result_shuffle = random.shuffle(result) # shuffling the result


Final_result = ''.join(result)

print(f"Your password is : {Final_result}") # with shuffled the random letters, numbers, symbols


# password generater in udemy explanation

import random
import numpy as np

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')','+']

print("Welcome to password generator")

num_letters = int(input("How many letters would you like in your password?\n "))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

password = []

for char in range(0,num_letters):
    password.append(random.choice(letters))

for char in range(0,num_numbers):
    password.append(random.choice(numbers))

for char in range(0,num_symbols):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)

password_final = ""
for char in password:
    password_final += char

print(password_final)


#Day 6
#Functions
#predefined functionss

#eg. print() , len()

#1.Defining Functions

#def my_function():
   #do this
   #then do this
   #finally do this

#2.Calling functions
#my_function()

#while loop

#def if_something_true:
    #do this repeatedly

#note: this loop will stop only the condition is false

#Day 7

#Hangman game

import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.


    if guess in correct_letters:
        print(f"you already guessed this letter: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py

    print(stages[lives])

#Exercise : 7
#life in weeks 

Life_years = 90

def life_in_weeks(age):
    Life_weeks_left = (90 - age) * 52
    print(f"you have {Life_weeks_left} weeks left ")
    
#calling the function
life_in_weeks(56)

# positional Argument 
#syntax 

#def my_function(a,b,c):
   #do this with a
   #then do this with b 
   #finally do this with c

#my_function(1,2,3)
#here a = 1 , b= 2, c =3.
# if we assign like 
#my_function(3,1,2)
#here a = 3 , b= 1, c =2.

# Arguments should be in the order of parameter
#in below example name and location is parameters and "Jack Bauer","chennai" is arguments

def greet_with_name(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_name("Jack Bauer","chennai")


#Keyword argument
#syntax 

#def my_function(a,b,c):
   #do this with a
   #then do this with b 
   #finally do this with c

#my_function(c=1,a=2,b=3)
#here we are defining with keyword so position changes also no problem.


#Day 8

#Functions with Inputs Arguments & parameters

#functions with inputs
#def function(someinput):
    #do this with someinput

#function(someinput) #we can provide the input inside the parantheses of the function.

#someinput = 123
#parameter = argument
#Exercise : 8
#love Calculator
def calculate_love_score(name_one,name_two):
    number_of_True = ["t", "r", "u", "e"]
    number_of_Love = ["l", "o", "v", "e"]
    true_count = 0
    love_count = 0
    name_one = name_one.lower()
    name_two = name_two.lower()
    
    for letter in number_of_True:
        true_count += name_one.count(letter) + name_two.count(letter)
            
    for letter in number_of_Love:
        love_count += name_one.count(letter) + name_two.count(letter)
        
            
    # Calculate total score
    total_score = str(true_count) + str(love_count)
    
    print(total_score)
    
    
calculate_love_score("Kanye West","Kim Kardashian")

#Caesar Cipher
# create the encrypt and decrypt functions

'''
part :1
TODO-1:
Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.

TODO-3:
Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.

TODO-4:
What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?

part :2
TODO-1:
Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.
 
TODO-3:
Combine the encrypt() and decrypt() functions into a single function called caesar().
Use the value of the user chosen direction variable to determine which functionality to use.
call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

part :3
TODO-1:
Import and print the logo from art.py when the program starts.

TODO-2:
What happens if the user enters a number/symbol/space that's not in the List alphabet?

Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

Can you figure out a way to restart the cipher program?

'''

from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    run = input("do you want to repeat the game?, type 'yes' or 'no'\n").lower
    if run == 'no':
        run_again = False
        print("Game over!")


#Day 9

#Dictionaries 
#syntax = dictionary_name {key : value , key : value} 
programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" :"A piece of code that you can easily call over and over again",
    "Loop" : "The action of doing something over and over again"
}

#Retrieving items from dictionary
print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"


#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#Exercise : 9

#scrore into grades

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 91 and student_scores[key] < 100 :
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 81 and student_scores[key] < 90 :
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 71 and student_scores[key] < 80 :
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

    #print(student_scores[key])
print(student_grades)



##Nesting

# list and dictionaries putting inside the dictionary 
# a sample nesting 
# {
# Key : [list]
# key : {Dic}
# } 

#Nesting
Capitals = {
   "France" : "Paris",
   "Germany" : "Berlin"
}

#Nesting a list in a dictionary

travel_vlog = {
    "France" : ["Paris","Lille","Dijon" ],
    "Germany" : ["Berlin", "Hamburg","Stuttgart"]
}

#print "Lille"

print(travel_vlog["France"][1])

#Nesting a dictionary in a dictionary

travel_vlog = {
    "France" :{
        "city_visited":["Paris","Lille","Dijon" ] ,
        "total_visits" : 3 
        },
    "Germany" : {
        "city_visited": ["Berlin", "Hamburg","Stuttgart"],
        "total_visits" : 5 
         }
}
#Print "stuttgart"
print(travel_vlog["Germany"]["city_visited"][2])

#Nesting a dictionary in a List

travel_vlog = [
    {
    "Country" :"France" ,
    "city_visited":["Paris","Lille","Dijon" ] , 
    "total_visits" : 3 
    },
   { 
    "Country" : "Germany" ,
    "city_visited": ["Berlin", "Hamburg","Stuttgart"],
    "total_visits" : 5 
    }
]


#blind bid program challenge 



#day 10
#Functions with outputs

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name}{formated_l_name}"#the return keyword will store the result of this function where the function called.

formated_string = format_name("Logeshwari","G") 

#Multiple return values












