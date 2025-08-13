# Week Four Assignment: File Operations in Python Programming
# This script demonstrates file operations in Python, including creating, reading, and writing to files.
import os

def read_and_modify_file():
    # Create a new file
    with open('Week_four.txt', 'w') as file:
        file.write("This is week Four assingment and we are learning about file operations in Python Programming!")

    # Read the content of the file
    with open('Week_four.txt', 'r') as file:
        content = file.read()

    # Write to an existing file
    with open('Week_four.txt', 'a') as file:
        file.write("\nThis is a new line.")

def handle_error(filename):
    try:
        with open(filename, 'r') as file:
            print(f"File '{filename}' exists and can be read.")
            # You can add code here to read the file if needed
    except FileNotFoundError:
        
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"Error: Could not read file '{filename}'. {e}")

if __name__ == "__main__":
    read_and_modify_file()
    #Read & Write:
    print("\nError Handling:")
    handle_error("example.txt")

