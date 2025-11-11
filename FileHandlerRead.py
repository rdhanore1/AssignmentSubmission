# 4. Read from a File
# We used open in read mode and file.read to read and print to display.

def read_from_file(filename: str) -> None:
    """Read content from a text file and print it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content of '{filename}':\n")
        print(content)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except IOError as exception:
        print(f"An error occurred while reading the file: {exception}")

def main() -> None:
    """Main function to get filename from user and read from file."""
    filename = input("Enter the filename to read (with .txt extension): ").strip()
    read_from_file(filename)

if __name__ == "__main__":
    main()

# Example usage:
# Enter the filename to read (with .txt extension): example.txt
# Content of 'example.txt':
# Hello, this is a test file.
# This will read and display the content of 'example.txt' if it exists.
