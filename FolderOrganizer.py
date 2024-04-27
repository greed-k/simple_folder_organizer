import os
import shutil

root_path = os.getcwd()

# def functions

#function to create new folders if it does not exist in the directory
def createFolder(folder_name):
    # there should already be a precheck to see if the folder exists before calling this function
    path = os.path.join(root_path, folder_name)
    os.mkdir(path)
    print('New folder made.')

def findFolder(folder_name):
    print('This is the folder name')


def moveFiles(origin , destination):
    # the goal of this is to move the object that is stated to the location that is stated


    print('Completed Move')

def generateTree():

    print()

def generateList():

    print()

def handleCommand(command):

    # process the command first
    command.lower() # lower case everything first
    commands = command.split(' ')
    match commands[0]:
        case "move":
            print('Enter the file name to move (Must be in the same folder):')
            filename = input()
            print('Enter the destination folder:')
            foldername = input()   
            # check if the file and the destination folder exists
            file_path = os.path.abspath(filename)
            if(os.path.exists(file_path) != 1):
                return
            else:
                print('The file does not exist.')
        case "exit": 
            exit

        case "list": # shows a list of all the files that is in the directory without any hierarchy 

            print()
        case "tree": # shows a tree of all the files from the root folder of where the python file was executed.

            print()

    print('Command Processed')

# main program 
print('Folder Organizer v0.1')
print('Key in "help" to get a list of commands.')
while 1:
    input = input()
    handleCommand(input)

    print('Key in "exit" to stop the program')
    input = input()
    if(input.lower() == "exit"):
        exit
    
    print('Key in a new command.')

