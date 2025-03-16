#imports
import subprocess #module allows to start external programs
import os
import sys
import time


#opening program func
def open_program(program_pathway):
    try:
        #try == trying to execute subprocess.Popen
        subprocess.Popen(program_pathway, shell=True) #subprocess.Popen is a function that starts a new process (opens a program)
        #shell = True allows the system commands to run as if they were in a terminal or cmd prompt..
        print(f"OPENING {program_pathway}")
    except Exception as e:
        #except catches any errors that would occur
        print(f"ERROR OPENING {program_pathway}") #also using f-string to embed var like {program_pathway}


def call_store():
    print("info store has been called")
    return

