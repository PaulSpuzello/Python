"""
Program: student.py
Author: Paul Spuzello
Last date modified: 03/24/2020

The purpose of this program is to create a student class and along with exception handling, unit test
the inputs such as if they are entered incorrectly.
"""

class Student:
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major

        self.gpa = gpa
        x = isinstance(gpa, int)
        if x == True and gpa < 0 or gpa > 4:
            raise ValueError

    def __str__(self):
        try:
            return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
        except ValueError:
            print("Error found, student not created")
