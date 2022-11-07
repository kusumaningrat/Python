import random, time

number = random.randint(1, 50)
def start():
    global name
    name = input("What's your name ? ")
    print("Hello ", name + " We are going to play game")
    time.sleep(1)
    print("Let's go")

def guess():
    guesstaken = 0

    while guesstaken < 6:
        user_input = int(input("Enter a number from range (1-50): "))

        if user_input <= 50 and user_input >= 1:
            guesstaken += 1

            if user_input < number:
                print("The number you guess to low.")
            if user_input > number:
                print("The number you guess to high.")
            if user_input != number:
                print("Try again!")
            if user_input == number:
                print("Good job ", name, "you guessed my number")

        if user_input > 50 or user_input < 1:
            print("Invalid number, please enter between range (1-50)")

    print("You have reached out your coin")

def repeat():
    repeat = input("Do you want to repeat ? (y/n)")    
    if repeat == "y":
        start()
        guess()
        repeat = input()

start()
guess()
repeat()