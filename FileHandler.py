# 3.Write to a File
# Write a program to create a text file and write some content to it.
#
# Using file functions like write and open.

def write_to_file(filename: str, content: str) -> None:
    """Create a text file and write content to it."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content written to '{filename}' successfully.")
    except IOError as exception:
        print(f"An error occurred while writing to the file: {exception}")

def main() -> None:
    """Main function to get filename and content from user and write to file."""
    filename = input("Enter the filename (with .txt extension): ").strip()
    content = input("Enter the content to write to the file: ").strip()
    write_to_file(filename, content)

if __name__ == "__main__":
    main()

# Example usage:
# Enter the filename (with .txt extension): example.txt
# Enter the content to write to the file: Hello, this is a test file.
# Content written to 'example.txt' successfully.
# This will create a file named 'example.txt' with the specified content.
