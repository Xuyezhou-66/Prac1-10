"""
Name:Xuyezhou
Date: 2021/09/07
Brief Project Description: main function
GitHub URL: https://github.com/Xuyezhou-66/ASS2.git
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from placecollection import PlaceCollection


class TravelTrackerApp(App):
    def __init__(self, **kwargs):
        """
        Install all the widgets in kivy app
        """
        self.FILENAME = 'places.csv'
        #  You might like to consider using a dictionary to help with mapping the GUI text to the attributes of the class to be sorted by.
        self.text2attr = {'Name': 'name', 'Priority': 'priority', 'Visited': 'is_visited', 'Country': 'country'}
        self.title = "Places to Visit 2.0 by Xuyezhou"
        super().__init__(**kwargs)
        # The data (model) for this program should be a single PlaceCollection object.
        self.place_collection = PlaceCollection()
        # The status bar at the top shows the number of places still to visit.
        self.top_place_status_label = Label(
            text="Places to visit: {}".format(self.place_collection.get_unvisited_num()))
        self.bottom_place_status_label = Label(text=self.title)
        # Sorting by the label
        self.sort_by_label = Label(text="Sort by:")
        # sort by the is_visited attribution default
        # The left side of the screen contains a drop-down "spinner" for the user to choose the sorting
        self.spinner = Spinner(text='Visited', values=('Visited', 'Country', 'Name', 'Priority'))
        self.add_new_place_label = Label(text="Add New Place...")
        self.place_name_label = Label(text="Name:")
        self.place_name_text_input = TextInput(write_tab=False, multiline=False)
        self.place_country_label = Label(text="Country:")
        self.place_country_text_input = TextInput(write_tab=False, multiline=False)
        self.place_priority_label = Label(text="Priority:")
        self.place_priority_text_input = TextInput(write_tab=False, multiline=False)

        # Add place and clear labels
        self.add_place_button = Button(text='Add Place')
        self.clear_button = Button(text='Clear')

    def build(self):
        """
        Open the kivy app and implement all widgets
        """
        #  The program should load the CSV file of places using the method from PlaceCollection.
        self.root = Builder.load_file('app.kv')
        self.place_collection.load_places(self.FILENAME)
        self.place_collection.sort('is_visited')
        self.left_panel_widgets()
        self.right_panel_widgets()
        return self.root

    def left_panel_widgets(self):
        """
        Build left panel and add widgets to it
        """
        # left
        self.root.ids.left_panel.add_widget(self.sort_by_label)
        self.root.ids.left_panel.add_widget(self.spinner)
        self.root.ids.left_panel.add_widget(self.add_new_place_label)
        self.root.ids.left_panel.add_widget(self.place_name_label)
        self.root.ids.left_panel.add_widget(self.place_name_text_input)
        self.root.ids.left_panel.add_widget(self.place_country_label)
        self.root.ids.left_panel.add_widget(self.place_country_text_input)
        self.root.ids.left_panel.add_widget(self.place_priority_label)
        self.root.ids.left_panel.add_widget(self.place_priority_text_input)
        self.root.ids.left_panel.add_widget(self.add_place_button)
        self.root.ids.left_panel.add_widget(self.clear_button)
        self.root.ids.top_panel.add_widget(self.top_place_status_label)
        # bind sort function
        self.spinner.bind(text=self.sort_place)
        # bind add place error check function
        self.add_place_button.bind(on_release=self.error_checker)
        # bind clear_text function
        self.clear_button.bind(on_release=self.clear_text)

    def right_panel_widgets(self):
        """
        Build right panel and add widgets to it
        """
        # right widgets
        # Set the top place status label
        self.top_place_status_label.text = "Place To visit: {}".format(self.place_collection.get_unvisited_num())

        # add all places to the right panel
        for place in self.place_collection.places:
            # The right side contains a button for each place, colour-coded based on whether the place is visited or not (the actual colour scheme is up to you).
            if place.is_visited:
                place_item = Button(
                    text='{} in {}, priority {} (visited)'.format(place.name, place.country, place.priority))
                place_item.id = place.name
                place_item.background_color = [0, 0, 0, 0.3]
            else:
                place_item = Button(text='{} in {}, priority {}'.format(place.name, place.country, place.priority))
                place_item.id = place.name
                place_item.background_color = [3, 168, 158, 0.3]
            # bind place click event
            # When the user clicks on a place button, the place changes between visited andunvisited
            place_item.bind(on_release=self.place_click)
            self.root.ids.right_panel.add_widget(place_item)

    def sort_place(self, *args):
        """
        Sort the places according to the user's choice
        """

        self.place_collection.sort(self.text2attr[self.spinner.text])
        self.root.ids.right_panel.clear_widgets()
        self.right_panel_widgets()

    def place_click(self, button):
        """
        Organize the status of the selected place
        """
        # visit the place
        if not self.place_collection.get_place_by_name(button.id).is_visited:
            self.place_collection.get_place_by_name(button.id).is_visited = True
            self.root.ids.bottom_panel.text = "You visited {}. Great travelling!".format(
                self.place_collection.get_place_by_name(button.id).name)
        # not visit the place
        else:
            self.place_collection.get_place_by_name(button.id).is_visited = False
            self.root.ids.bottom_panel.text = "You need to  visite {}".format(
                self.place_collection.get_place_by_name(button.id).name)
        # update the right_panel
        self.sort_place()
        self.root.ids.right_panel.clear_widgets()
        self.right_panel_widgets()

    def clear_text(self, *args):
        """
        Clear all text fields
        """
        self.place_name_text_input.text = ""
        self.place_country_text_input.text = ""
        self.place_priority_text_input.text = ""
        self.root.ids.bottom_panel.text = ""

    def error_checker(self, *args):
        """
        To check if the input is valid or not
        """
        # no empty input
        if self.place_name_text_input.text == '' \
                or self.place_country_text_input.text == '' \
                or self.place_priority_text_input.text == '':
            self.root.ids.bottom_panel.text = "All fields must be completed"
        else:
            try:
                priority = int(self.place_priority_text_input.text)
                # priority > 0
                if priority <= 0:
                    self.root.ids.bottom_panel.text = "Priority must be > 0"
                # correct input
                else:
                    self.place_collection.add_new_place(self.place_name_text_input.text,
                                                        self.place_country_text_input.text,
                                                        priority)
                    self.place_collection.sort(self.text2attr[self.spinner.text])
                    self.clear_text()
                    self.root.ids.right_panel.clear_widgets()
                    self.right_panel_widgets()
            # priority input must be a number
            # The status bar at the bottom shows program messages.
            except ValueError:
                self.root.ids.bottom_panel.text = "Please enter a valid number"

    def stop(self):
        """
        The places file must be saved (there's a method for that!) when the program ends,
        updating any changes made with the app by the user
        """

        self.place_collection.save_places(self.FILENAME)


if __name__ == '__main__':
    TravelTrackerApp().run()
