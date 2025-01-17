
def main():
    instructions = """
    This CLI supports two functions:
    - GET : retrieve the contents of an existing file
    - SET : create and set the contents of a new file OR update the contents of an existing file
    """
    print(instructions)
    command = input("Please enter either 'GET' or 'SET': ")
    print("You entered: ", command)
    filename = input("Please enter your filename: ")  # TODO: retrieve file contents of a file outside current directory?
    print("You entered: ", filename)
    if command == "SET":
        print("Please enter the contents of your file: ")

if __name__ == "__main__":
    main()
