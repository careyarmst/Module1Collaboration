# Author: Carey Armstrong
# Date: 29 October 2024
# Version: 3.0
# Purpose: Enter student name & GPA and determine honor roll status
# Initialize Student class
class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class Honors(Student):
    def __init__(self, fname, lname, GPA, honor_output):
        super().__init__(fname, lname)
        self.GPA = GPA
        self.honor_output = honor_output


def get_student_dta():
    fname = input("Enter Student's first name: ")
    if fname == "ZZZ":
        print("Thanks for using our program!!")
        quit(0)
    else:
        lname = input("Enter Student's last name: ")
    return fname, lname


def get_honors_dta():
    GPA = float(input("Enter the student's GPA: "))
    if GPA > 3.5:
        honor_output = "Dean's List"
    if GPA > 3.25 and GPA < 3.5:
        honor_output = "Honor Roll"
    if GPA < 3.25:
        honor_output = "None"
    return GPA, honor_output

def main():
    getstud = Student('fname', 'lname')
    while getstud.fname != "ZZZ":
        hnrstudent = Honors(*get_student_dta(), *get_honors_dta())
        print(
            f"Honor Student Name: {hnrstudent.fname} {hnrstudent.lname}, Student GPA: {hnrstudent.GPA}, Honor Student Status: {hnrstudent.honor_output}")

main()
