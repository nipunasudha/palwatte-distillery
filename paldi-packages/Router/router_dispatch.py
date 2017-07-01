import os


def run_service(relPathr):
    os.system("start cmd /K python " + relPathr)
    print("Server process launched as a seperate process.")
