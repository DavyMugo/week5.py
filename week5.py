def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("This is line 3 with a mix of strings and numbers.\n")
    except FileNotFoundError:
        print("FileNotFoundError: The specified file path was not found.")
    except PermissionError:
        print("PermissionError: Permission denied to create the file.")
    finally:
        print("File creation process completed.")

def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("FileNotFoundError: The specified file path was not found.")
    except PermissionError:
        print("PermissionError: Permission denied to read the file.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 4.\n")
            file.write("56789\n")
            file.write("This is the fifth line being appended.\n")
    except FileNotFoundError:
        print("FileNotFoundError: The specified file path was not found.")
    except PermissionError:
        print("PermissionError: Permission denied to append to the file.")
    finally:
        print("Appending process completed.")

# Create the file
create_file()

# Read and display the contents of the file
read_and_display_file()

# Append to the file
append_to_file()
