
import sys
import os

bufferSize = 4096

def main():
    
    instructions = """
    This CLI supports two functions:
    - GET : retrieve the contents of an existing file
    - SET : create and set the contents of a new file OR update the contents of an existing file

    Please note: this program only supports text files.
    """
    
    print(instructions)
    
    command = input("Please enter either 'GET' or 'SET': ").upper()
    if command != "GET" and command != "SET":
        sys.exit("\nInvalid command entered. Exiting program...")

    filename = input("Please enter your filename: ")

    if command == "GET":
        try:
            with open(filename, "r") as file:
                print(f"\nReading from: {os.path.basename(filename)}...\n")
                for line in file:
                    print(line.strip())
        except Exception as e:
            sys.exit(f"\nError: {e}\nExiting program...")
            handleGet(filename)

    elif command == "SET":
        print("Please enter the contents of your file: (Ctrl + D to save)")
        try:
            with open(filename, "w") as file:
                for line in sys.stdin:
                    file.write(line)
                    file.flush()
            print(f"\nInput written to {filename}. Exiting program...")
        except Exception as e:
            sys.exit(f"\nError: {e}\nExiting program...")

    else:
        sys.exit("\nUnknown error. Exiting program...")

if __name__ == "__main__":
    main()
