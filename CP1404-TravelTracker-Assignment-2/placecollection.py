"""
Name: Xuyezhou
Date: 2021/09/07
Brief Project Description:
This class should contain a single attribute: a list of Place objects.
GitHub URL: https://github.com/Xuyezhou-66/ASS2.git
"""

# Create your PlaceCollection class in this file
from place import Place


class PlaceCollection:
    """
    This class should contain a single attribute: a list of Place objects, and at least the following methods:
    """

    def __init__(self):
        """
        Constructor function
        """
        self.FILENAME = 'places.csv'
        self.places = []

    def sort(self, key):
        if key == 'name':
            self.places.sort(key=lambda x: (x.name, x.priority))
        if key == 'country':
            self.places.sort(key=lambda x: (x.country, x.priority))
        if key == 'is_visited':
            self.places.sort(key=lambda x: (x.is_visited, x.priority))
        if key == 'priority':
            self.places.sort(key=lambda x: x.priority)


    def get_unvisited_num(self):
        """
        get number of unvisited places
        :return: count of unvisited places
        """
        # initial count variable to 0
        count = 0
        # traverse the places
        for place in self.places:
            if not place.is_visited:
                count += 1
        return count

    def save_places(self, filename):
        """
        save places (from place list into csv file)
        """
        with open(filename, mode='w') as f:
            # traverse all the places
            for place in self.places:
                if place.is_visited:
                    f.write(','.join([place.name, place.country, str(place.priority), 'v']) + '\n')
                else:
                    f.write(','.join([place.name, place.country, str(place.priority), 'n']) + '\n')
        print('{} places saved to places.csv\nHave a nice day :)'.format(len(self.places)))

    def load_places(self, filename):
        """
        load places (from csv file into Place objects in the list)
        """
        # define constant variable
        VISIT = 'v'
        NOTVISIT = 'n'
        count = 0
        with open(filename) as f:
            line = f.readline().strip()
            # read line
            while (line):
                # extra name attribution
                name = line.split(',')[0]
                # extra country attribution
                country = line.split(',')[1]
                # extra priority attribution
                try:
                    priority = int(line.split(',')[2])
                except ValueError:
                    continue
                # extra has_visit attribution
                is_visited = line.split(',')[3]
                # convert has_visit to boolean
                if is_visited == VISIT:
                    is_visited = True
                elif is_visited == NOTVISIT:
                    is_visited = False
                if name == '' or country == '':
                    continue
                # construct place object
                place = Place(name, country, priority, is_visited)
                # add place to places list
                self.places.append(place)
                count += 1
                # read next line
                line = f.readline().strip()
        print('{} places loaded from places.csv'.format(count))

    def add_place(self, place):
        """
         add place to places list
        """
        self.places.append(place)

    def get_place_by_name(self, name):
        """
        get the place by name
        :return: place
        """
        for place in self.places:
            if place.name == name:
                return place
    def add_new_place(self, name, country, priority):
        """
        add new place to places
        :param name: name of place
        :param country: name of city
        :param priority:  name of priority
        """
        place = Place(name, country, priority, False)
        self.places.append(place)
