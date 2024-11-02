# Assignment M02 SDEV 220 STUDENT GPAs
# Author: Carey Armstrong
# Version: 5.0
# Date: 2024-11-02
# Initialize Student class
class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# Initialize Honors class
class Honors(Student):
    def __init__(self, fname, lname, GPA, honor_output):
        super().__init__(fname, lname)
        self.GPA = GPA
        self.honor_output = honor_output

# Function to get the student's name
def get_student_dta():
    fname = input("Enter Student's first name: ")
    if fname == "ZZZ":
        print("Thanks for using our program!!")
        quit(0)
    else:
        lname = input("Enter Student's last name: ")
    return fname, lname

# Function to get the student's GPA and honor status
def get_honors_dta():
    try:
        GPA = float(input("Enter the student's GPA: "))
        if GPA > 3.5:
            honor_output = "Dean's List"
        if GPA > 3.25 and GPA < 3.5:
            honor_output = "Honor Roll"
        if GPA < 3.25:
            honor_output = "None"
        if GPA > 4.0 or GPA < 0.0:
            honor_output = "That value is too large or too small for a GPA"
    except ValueError:
           print("Value entered is not a float")
           exit(0)
    return GPA, honor_output

# Function to put the other functions together/main function
def main():
    getstud = Student('fname', 'lname')
    while getstud.fname != "ZZZ":
        hnrstudent = Honors(*get_student_dta(), *get_honors_dta())
        print(
            f"Honor Student Name: {hnrstudent.fname} {hnrstudent.lname}, Student GPA: {hnrstudent.GPA}, Honor Student Status: {hnrstudent.honor_output}")

main()
