import subprocess
import os


def run_server(relPath):
    os.system("start cmd /K python "+relPath)

    # subprocess.Popen("run.bat", shell=True)
    print("Server process launched as a seperate process.")
