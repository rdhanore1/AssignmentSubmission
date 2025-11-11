# 2 Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.
# Used dictionary and basic operations. Using if else:

def add_or_update_student(grades: dict, name: str, grade: str) -> None:
    """Add a new student or update an existing student's grade."""
    grades[name] = grade
    print(f"Student '{name}' has been added/updated with grade '{grade}'.")

def print_all_grades(grades: dict) -> None:
    """Print all student grades."""
    if not grades:
        print("No student grades available.")
        return
    for name, grade in grades.items():
        print(f"{name}: {grade}")

def main() -> None:
    """Main function to manage student grades."""
    grades = {}

    while True:
        print("\nOptions:")
        print("1. Add/Update Student Grade")
        print("2. Print All Student Grades")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            grade = input("Enter student grade: ").strip()
            add_or_update_student(grades, name, grade)
        elif choice == "2":
            print_all_grades(grades)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

# Example usage:
# Options:
# 1. Add/Update Student Grade
# 2. Print All Student Grades
# 3. Exit
# Choose an option (1-3): 1
# Enter student name: Alice
# Enter student grade: A
# Student 'Alice' has been added/updated with grade 'A'.


