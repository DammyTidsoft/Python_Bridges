# file_handling_assignment.py

def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("First line of text.\n")
            file.write("1234567890\n")
            file.write("Another line of text with numbers 9876.\n")
        print("File created and written to successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("Contents of the file:")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appended line one.\n")
            file.write("Appending more text.\n")
            file.write("Final appended line 45678.\n")
        print("Text appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()
