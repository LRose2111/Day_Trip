

# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

#1 Store the trip options for destinations, restaurants, transportation, and entertainment in a List

import random


destination_list = ['england', 'toronto', 'miami']

restuarant_list = ['bistro', 'pizza', 'diner']

transportation_list = ['helicopter', 'taxi', 'subway']

entertainment_list = ['comedy show', 'concert', 'sporting event']

# Get a random element from each of those sets of options. We recommend declaring variables for a random destination, restaurant, transportation, and entertainment

# Initial function

#note- orginal random function didnt work, try with each list seperatly.

def get_choice(choice_list, choice_type):
    random_choice = '0'
    previous_choice = '0'
    user_confirmation = 'n'
    while user_confirmation == 'n':
        random_choice = random.choice(choice_list)
        if previous_choice == random_choice:
            continue
        user_confirmation = input(f'{random_choice} has been selected, Does this sound good? y/n ?')
        if user_confirmation == 'y':
            print(f'Lets check out the {choice_type} now.')
        if user_confirmation == 'n':
            print('Lets try again.')
            previous_choice = random_choice

    return(random_choice)

def run_trip_gen():
    user_conformation = 'n'
    while user_conformation == 'n':
        
        destination_list = '0'
        if destination_list == destination:
            destination = get_choice(destination_list, 'destination')
        
        restuarant_list = '0'
        if restuarant_list == restuarant:
             restuarant = get_choice(restuarant_list, 'restuarant')
        
        entertainment_list = '0'
        if entertainment_list == entertainment:
             entertainment = get_choice(entertainment_list, 'entertainment')
        
        transportation_list = '0'
        if transportation_list == transportation:
            transportation = get_choice(transportation_list, 'transportation')

user_confirmation = input(f'You will be going to {destination_list}, have a great time at the {entertainment_list}, followed by a nice meal at{restuarant_list}. You will be using {transportation_list} to get around! Does tthis sound good? y/n ?')
if user_confirmation == 'y':
    print('Have a great trip!')
if user_confirmation == 'n':
    print('Lets try again.')

run_trip_gen()

