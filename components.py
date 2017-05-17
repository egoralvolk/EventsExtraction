class Date:
    def __init__(self):
        self.day_of_week = ""
        self.designation = ""
        self.time_of_day = ""
        self.day = ""
        self.month = ""
        self.year = ""
        self.century = ""
        self.millenium = ""
        self.in_text = ""

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self.day_of_week, self.designation, self.time_of_day, self.day,
                                                        self.month, self.year, self.century, self.millenium)


class Toponym:
    def __init__(self):
        self.name = ""
        self.latitude = None
        self.longitude = None
        self.link_to_article = None

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return other.name == self.name


class Person:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.patron = ""
        self.link_to_article = None

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.patron


class Event:
    def __init__(self, date, sentence):
        self.date = date
        self.sentence = sentence
        self.toponyms = []
        self.persons = []

    def __str__(self):
        out = '----------\nEvent\nDate: ' + str(self.date) + '\nToponyms:'
        for t in self.toponyms:
            out += '\n' + str(t)
        out += '\nPersons:'
        for p in self.persons:
            out += '\n' + str(p)
        return  out + "\nSentence: " + self.sentence

