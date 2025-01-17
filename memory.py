
import sys
import os

def handleGet(filename):
    print(filename)

def handleSet(filename):
    print(filename)

def main():
    
    instructions = """
    This CLI supports two functions:
    - GET : retrieve the contents of an existing file
    - SET : create and set the contents of a new file OR update the contents of an existing file
    """
    
    print(instructions)
    
    command = input("Please enter either 'GET' or 'SET': ").upper()
    if command != "GET" and command != "SET":
        sys.exit("\nInvalid command entered. Exiting program...")

    filename = input("Please enter your filename: ")

    if command == "GET":
        if not os.path.isfile(filename):
            sys.exit("\nFile does not exist. Exiting program...")
        handleGet(filename)
        
    elif command == "SET":
        print("Please enter the contents of your file: ")
        handleSet(filename)

if __name__ == "__main__":
    main()
