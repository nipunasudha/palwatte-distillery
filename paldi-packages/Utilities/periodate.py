import urllib.request
import time
import pprint
import os

clear = lambda: os.system('cls')

while True:
    clear()
    print("=============================================")
    print("=============================================")
    print("          IMAGE CAPTURE PERIODATER           ")
    print("=============================================")
    print("=============================================\n")
    try:
        result = urllib.request.urlopen("http://localhost:5000/get-ocr").read()

    except:
        result = "Error connecting to the server!"
    else:
        print("Trigger successful.")

    pprint.pprint(result)
    time.sleep(5)
