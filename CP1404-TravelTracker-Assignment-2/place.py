"""
Name: Xuyezhou
Date: 2021/09/07
Brief Project Description:
This should be a simple class with the required attributes for a place (name, country,
priority and visited status)
GitHub URL: https://github.com/Xuyezhou-66/ASS2.git
"""


class Place:
    """
    This should be a simple class with the required attributes for a place (name, country,
    priority and visited status)

    """

    def __init__(self, name = '', country='', priority=0, is_visited=False):
        """
        Constructor function
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        """
        str function
        :return: str
        """
        return 'Places, name: {}, country: {}, priority: {}, is_visited: {}'.format(
            self.name, self.country, self.priority, self.is_visited)

    def visit(self):
        """
         mark the place as visited
        :return:
        """
        self.is_visited = True

    def unvisit(self):
        """
         mark the place as unvisited
        :return:
        """
        self.is_visited = False

    def important(self):
        """
        a method to determine if a place is considered "important", which is defined as
        having a priority <= 2.
        :return:
        """
        return self.priority <= 2


p = Place()
