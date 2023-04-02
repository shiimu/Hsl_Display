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

answer = input("Option[Y(es)/N(o)]: ")

if answer == "Y":
    print("Starting")
elif answer == "N":
    print("Exiting")
else:
    print("error")
