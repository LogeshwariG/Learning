

#blind bid program
bidders = {}
bid_conti = True

while bid_conti == True:
    name = input("Type your name \n")
    bid = int(input("Type your bid amount \n$"))
    bidders[name] = bid
    
    bid_count = input("do you want to bid again? Type yes or no ").lower
    if bid_count == "no":
        bid_conti == False
    else:
        exit()
    #print(bid_count)

print(bidders)

'''
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





#love calculator 

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


#life in weeks 

Life_years = 90

def life_in_weeks(age):
    Life_weeks_left = (90 - age) * 52
    print(f"you have {Life_weeks_left} weeks left ")
    
#calling the function
life_in_weeks(56)


#hangman 

import random

#To do-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
lives = 6

# To do-3: - Import the logo from hangman_art.py and print it at the start of the game.
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

    # To do-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # To do-4: - If the user has entered a letter they've already guessed, print the letter and let them know.


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

    # To do-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True

            # To do 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # To do-2: - Update the code below to use the stages List from the file hangman_art.py

    print(stages[lives])

# password generating udemy explanation

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



# password generating my practice 

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

print(final_result)

result_shuffle = random.shuffle(result)

Final_result = ''.join(result)

print(f"Your password is : {Final_result}")




# Fizz and Buzz game

for number in range(1, 101):
    if (number % 3) == 0 and (number % 5) == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


#print range

total = 0

for number in range(1, 101):
   total += number
print(total)

# print highest value

student_scores = [180, 124, 165, 173, 189, 169, 146]
max = 0
for score in student_scores:
   if max < score:
    max  = score
print(max)


#print random

import random

friends = ["mani" , "pavi" ,"Manju" ,"sangee" ,"loge" , "kala"]

print(random.choice(friends))
'''