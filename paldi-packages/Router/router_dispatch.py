import os


def run_server(relPath):
    os.system("start cmd /K python " + relPath)
    print("Server process launched as a seperate process.")
