# Alex Reiter
# Coding and Design
# 2/14/2023

import random, time, datetime

name = ''
age = -1

def sleep_loop(num_loops):
    for i in range(0,num_loops):
        print("...")
        time.sleep(0.5)

def display_wake_up():

    greetings = ['Waaaa, where am I?', 'Hey, who turned on the light?', 
    'Ah, I see you have come at last...']

    print(random.choice(greetings))
    sleep_loop(10)

def ask_for_name():

    name = input("What is your name, young one?")
    sleep_loop(2)
    print("Why, hello there, " + name + '.')
    sleep_loop(2)
    print("I've heard much about you...")
    sleep_loop(2)
    print("The legend foretells of one who will come to save us from the darkness...")
    sleep_loop(2)


def ask_for_number(scripts, errorMessage='', successMessage=''):
    got_valid_input = False
    num_attempts = 0

    while not got_valid_input:

        try:
            valid_input = int(input(scripts[num_attempts] + ' '))
            if successMessage != '':
                sleep_loop(2)
                print(successMessage)
            return valid_input

        except ValueError:
            if errorMessage != '':
                print(errorMessage)
            num_attempts+=1
            print(num_attempts)
            if (num_attempts > (len(scripts)-1)):
                num_attempts = len(scripts)-1

def calculate_age(current_year, birth_year):

    age_guess = current_year - birth_year
    age_script = ["Are you " + str(age_guess-1) + " or " + str(age_guess) + "?"]

    return ask_for_number(age_script)

def react_to_age(user_age):

    if user_age < 5:
        print("You seem very young for this quest...")

    elif user_age < 15:
        print("Many great heros start their journey young...")

    elif user_age < 25:
        print("Ahh, you are in your prime!")

    elif user_age < 40:
        print("You have some weariness to you, but still a glimmer of spirit.")

    elif user_age < 60:
        print("You are strong and yet full of wisdom")

    elif user_age < 80:
        print("You will use your wisdom to guide all others")

    else:
        print("You have transcended age")

def present_items(item_list):

    print("You may choose one of these items on your quest...")

    for index, item in enumerate(item_list):
        print("********* ~ ~ " + item + " ~ ~ ********* (Select " + str(index) + ")")

    sleep_loop(2)
    print("Which do you choose?")

    selection = ask_for_number(["Pick a number.", "Please make your choice in the form of a number."])

    sleep_loop(2)

    print("Ah, so you selected the " + item_list[selection] + ". Very well...")

    sleep_loop(2)
    return item_list[selection]


year_scripts = ["I've been asleep for a long while...Remind me...what year is it?",
    "Now...what year is it??",
    "I see you do not take the fate of our world seriously...what is the current year?",
    "I can wait all century...what is the year?"]
year_error = "Hmm...is that how our calendar system works?"
year_success = "Ahhh, is it really?!"

age_scripts = ["And what year were you born??", "Hrmm...what is your birth year???"]



display_wake_up()
ask_for_name()
current_year = ask_for_number(year_scripts, year_error, year_success)
sleep_loop(2)
birth_year = ask_for_number(age_scripts)
sleep_loop(2)
age = calculate_age(current_year, birth_year)
sleep_loop(4)
react_to_age(age)
sleep_loop(2)
present_items(["golden sword", "magic hammer", "silver wand", "enchanted cloak"])
sleep_loop(2)
print("You are now ready to go on your journey")
sleep_loop(4)
print("Now I must go")
sleep_loop(4)
print("POOF!!!")




