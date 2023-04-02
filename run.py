'''
Execution of the application
'''
print("Checking for constants.py")
# check here
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
    answer = input("Option[Y(es)/N(o)]: ")
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
except NameError:
    print("error")
