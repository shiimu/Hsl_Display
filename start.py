'''
Execution of the application
'''
import os

PATH = './hsl_display/test.py'

KEYS = '''
KEYS = {
        "OWM_KEY": "fcc250fd2a7a605c8269de49d1dc6dda",
        "HSL_KEY": ""
        }
'''


def create_file():
    """A dummy docstring."""
    with open(PATH, "x") as file:
        file.close()


def append_file():
    '''Dummy doctstring.'''
    with open(PATH, "a") as file:
        file.write(KEYS)
        file.close()


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


'''
file = "constants.py"
if file != constants.py:
    touch constants.py with:
        #API Keys
KEYS = {
        "OWM_KEY": "fcc250fd2a7a605c8269de49d1dc6dda",
        "HSL_KEY": ""
        }
COORDS = {
        "LAT": "60.23787",
        "LON": "25.10560"
        }
STOP_ID = {
        "STOP_1": "HSL:1472113"
        }
'''
# ask if want owm
# ask for long
# ask for lat
# ask if want hslkey
# ask for stop id
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
        # Make this into an object
        answer = input("Insert Open Weather Maps Key: ")
        with open(PATH, "a") as file:
            file.write('KEYS = {"OWM_KEY": "'+answer+'",')
            file.close()
        answer = input("Insert Lattitude: ")
        with open(PATH, "a") as file:
            file.write('"LAT": "'+answer+'",')
            file.close()
        answer = input("Insert Longitude: ")
        with open(PATH, "a") as file:
            file.write('"LON": "'+answer+'",')
            file.close()
        answer = input("Insert HSL Key: ")
        with open(PATH, "a") as file:
            file.write('"HSL_KEY": "'+answer+'",')
            file.close()
        answer = input("Insert Bus Stop ID: ")
        with open(PATH, "a") as file:
            file.write('"STOP_1": "'+answer+'"}')
            file.close()
    elif any(neg_answer):
        print("Exiting")
    elif any(res_answer):
        print("Restarting setup")

except NameError:
    print("error")
