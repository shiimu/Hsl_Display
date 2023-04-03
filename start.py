'''
Execution of the application
'''
import os

PATH = './hsl_display/test.py'


def create_file():
    """A dummy docstring."""
    with open(PATH, "x") as file:
        file.close()
    reconfigure_file()


def append_file(value):
    '''Dummy doctstring.'''
    with open(PATH, "a") as file:
        file.write(value)
        file.close()


def reconfigure_file():
    '''Dummy docstring.'''

    answer = input("Insert Open Weather Maps Key: ")
    append_file('KEYS = {"OWM_KEY": "'+answer+'",')
    answer = input("Insert Lattitude: ")
    append_file('"LAT": "'+answer+'",')
    answer = input("Insert Longitude: ")
    append_file('"LON": "'+answer+'",')
    answer = input("Insert HSL Key: ")
    append_file('"HSL_KEY": "'+answer+'",')
    answer = input("Insert Bus Stop ID: ")
    append_file('"STOP_1": "'+answer+'"}')


print("Checking for constants.py")
# check here.
try:
    if os.path.isfile(PATH):
        print("File exists")
    else:
        print("No file there")
        print("Creating file")
        create_file()
except NameError:
    print("Error")

# if not make one

print("Ready to start")
print("Do you want to start?")

try:
    answer = input("Option[Y(es)/N(o)/R(econfigure)]: ")
    pos_answer = [
            answer == "Y",
            answer == "y",
            answer == "Yes",
            answer == "yes"
            ]
    neg_answer = [
            answer == "N",
            answer == "n",
            answer == "No",
            answer == "no"
            ]
    res_answer = [
            answer == "R",
            answer == "r"
            ]
    if any(pos_answer):
        print("Starting")
    elif any(neg_answer):
        print("Exiting")
    elif any(res_answer):
        print("Restarting setup")
        reconfigure_file()
except NameError:
    print("error")
