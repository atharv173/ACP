#only for windows operating system
import os

def shutdown():
    os.system("shutdown /s /t 1")

shutdown()


#===========================================================================================================================


#for Windows, Linux and Darwin operating system


import os
import platform

def shutdown_system():
    current_os = platform.system()

    if current_os == "Windows":
        os.system("shutdown /s /t 1")

    elif current_os == "Linux" or current_os == "Darwin":
        os.system("sudo shutdown -h now")

    else:
        print("Unsupported Operating System")

shutdown_system()