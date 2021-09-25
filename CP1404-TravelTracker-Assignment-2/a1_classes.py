"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class


"""
Replace the contents of this module docstring with your own details
Name:Xuyezhou
Date started:2021/09/10
GitHub URL:https://github.com/Xuyezhou-66/ASS2.git
"""
import random
from place import Place
from placecollection import PlaceCollection

def display_menu():
    """
    display a menu for the user to choose from [2, 3]
    """
    print('Menu:')
    print('L - List places by Lindsay Ward')
    print('R - Recommend random')
    print('A - Add new place')
    print('M - Mark a place as visited')
    print('Q - Quit')


def display_places(places):
    """
    display all the places
    :param places: places list
    :return: unvisited_places list and visited_places list
    """
    VISIT = 'v'
    NOTVISIT = 'n'
    count_not_visit = 0
    places_len = len(places)
    visited_places = []
    unvisited_places = []
    # traverse the places
    for i in range(len(places)):
        place = places[i]
        # has visit
        if place[3] == VISIT:
            visited_places.append(place)
        # not has visit
        if place[3] == NOTVISIT:
            count_not_visit += 1
            unvisited_places.append(place)
        visited_places.sort(key=lambda x: x[2])
    unvisited_places.sort(key=lambda x: x[2])
    # not has visit
    for i in range(len(unvisited_places)):
        place = unvisited_places[i]
        print('*{}. {:<15}in {:<15}{:>3}'.format(i + 1, place[0], place[1], place[2], place[3]))
    # has visit
    for i in range(len(visited_places)):
        place = visited_places[i]
        print(' {}. {:<15}in {:<15}{:>3}'.format(len(unvisited_places) + i + 1, place[0], place[1], place[2], place[3]))
    print('{} places. You still want to visit {} places.'.format(places_len, count_not_visit))
    return unvisited_places + visited_places


def recommend_places(places):
    """
    recommend places to visit for random choice
    :param places: places list
    """
    NOTVISIT = 'n'
    print('Not sure where to visit next?')
    recommends = []
    for i in range(len(places)):
        place = places[i]
        # not has visit
        if place[3] == NOTVISIT:
            recommends.append(place)
    # random choose an unvisited place
    recommend_place = random.choice(recommends)
    print('How about... {} in {}?'.format(recommend_place[0], recommend_place[1]))


# You should be able to use generic, customisable functions to perform input with error checking
# (e.g., getting the place name and country can reuse the same function).
def get_input_name_country(hint):
    """
    generic function get the place name and country name in this function
    :param hint: hint infomation string
    :return: the input string
    """
    while (True):
        result = input(hint + ': ')
        # blank
        if (result == '' or result == None):
            print('Input can not be blank')
        else:
            return result


def count_unvisit(places):
    """
    count how many unvisited places in places list
    :param places:  places list
    :return: count of unvisited places
    """
    count_unvisit_num = 0
    # print(places)
    # No unvisited places
    for place in places:
        if place[3] == 'n':
            count_unvisit_num += 1
    return count_unvisit_num



# You should be able to use generic, customisable functions to perform input with
# error checking (e.g., getting the place name and country can reuse the same function).
def main():
    """
    main function
    """
    # display a welcome message with your name in it
    print("Travel Tracker 1.0 - by Xu Yezhou")
    # initial the place list
    # load a CSV (Comma Separated Values) file of places (just once at the very start);
    FILENAME = 'places.csv'
    places = PlaceCollection()
    places.load_places()
    while True:
        display_menu()
        choice = input('>>> ').upper()
        # error-check user inputs as demonstrated in the sample output [4]
        if choice not in ['L', 'R', 'A', 'M', 'Q']:
            print('Invalid menu choice')
        else:
            # quit the system
            # when the user chooses quit: save the places to the CSV file, overwriting the file contents
            # (note that this should be the only time that the file is saved)
            if choice == 'Q':
                places.save_places()
                break
            # recommend place
            if choice == 'R':
                count_unvisit_num = places.get_unvisited_num()
                if count_unvisit_num == 0:
                    print('No places left to visit!')
                else:
                    recommend_places(places)
            # add place
            if choice == 'A':
                name = get_input_name_country('Name')
                country = get_input_name_country('Country')
                while (1):
                    try:
                        priority = int(input('Priority: '))
                        break
                    except ValueError:
                        print('Invalid input!')
                print('{} in {} (priority {}) added to Travel Tracker'.format(name, country, priority))
                places.append([name, country, priority, 'n'])
            # list the place
            if (choice == 'L'):
                places = display_places(places)
            # mark the place
            if (choice == 'M'):
                # display the place list
                places = display_places(places)
                # count unVisit num
                count_unvisit_num = count_unvisit(places)
                # No unvisited places left
                if count_unvisit_num == 0:
                    print('No unvisited places')
                else:
                    print('Enter the number of a place to mark as visited')
                    while True:
                        try:
                            n = int(input('>>> '))
                            # invalid input
                            if n <= 0:
                                print('Number must be > 0')
                            elif n > len(places):
                                print('Invalid place number')
                            # already visited
                            elif (places[n - 1][3] == 'v'):
                                print('You have already visited {}'.format(places[n - 1][0]))
                                break
                            else:
                                places[n - 1][3] = 'v'
                                print('{} in {} visited!'.format(places[n - 1][0], places[n - 1][1]))
                                break
                        # not a number
                        except ValueError as e:
                            print('Invalid input; enter a valid number')


if __name__ == '__main__':
    main()
