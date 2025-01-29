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
