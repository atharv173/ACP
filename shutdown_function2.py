#safer version
#for Windows, Linux and Darwin operating system


import os
import platform

def shutdown_system():
    current_os = platform.system()

    confirm = input("Do you want to shutdown your computer ? (yes/no): ")
    if confirm.lower()== "yes":
        
        if current_os == "Windows":
            os.system("shutdown /s /t 1")

        elif current_os == "Linux" or current_os == "Darwin":
            os.system("sudo shutdown -h now")

        else:
            print("Unsupported Operating System")

    else:
        print("THEN WHY DID YOU CLICK THE RUN BUTTON. YOU FOOL !!")

shutdown_system()