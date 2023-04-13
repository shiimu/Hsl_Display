'''
Execution of the application
'''
import os
import subprocess

PATH = './hsl_display/constants.py'


def create_file():
    '''Create constants.py'''
    with open(PATH, "x") as file:
        file.close()
    reconfigure_file()


def append_file(value):
    '''Append to the end of constants.py'''
    with open(PATH, "a") as file:
        file.write(value)
        file.close()


def reconfigure_file():
    '''Reconfigure the constants.py file
    from the start'''

    answer = input("Insert Open Weather Maps key: ")
    append_file('KEYS = {"OWM_KEY": "'+answer+'",')
    answer = input("Insert Lattitude: ")
    append_file('"LAT": "'+answer+'",')
    answer = input("Insert Longitude: ")
    append_file('"LON": "'+answer+'",')
    answer = input("Insert HSL Key: ")
    append_file('"HSL_KEY": "'+answer+'",')
    answer = input("Insert Bus Stop id: ")
    append_file('"STOP_1": "'+answer+'"}')
    start_flask()


def start_flask():
    '''Start run_flask.py in ./hsl_display/ subfolder'''
    subprocess.run(["python3", "./hsl_display/run_flask.py"])


'''Check if constants.py exists
    if not create the file'''
print("Checking for constants.py")
try:
    if os.path.isfile(PATH):
        print("File exists")
    else:
        print("No file there")
        print("Creating file")
        create_file()
except NameError:
    print("Error")


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
        start_flask()
    elif any(neg_answer):
        print("Exiting")
    elif any(res_answer):
        print("Restarting setup")
        reconfigure_file()
except NameError:
    print("error")
