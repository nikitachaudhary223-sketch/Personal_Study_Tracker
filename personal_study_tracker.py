subjects = {}

def add_subject():
    subject = input("Enter subject: ").strip()

    if subject in subjects:
        print("Subject already exists!")
    else:
        subjects[subject] = 0
        print("Subject added successfully!")


def view_subjects():
    if len(subjects) == 0:
        print("No subjects added yet.")
    else:
        print("\nYour Subjects:")
        for subject, marks in subjects.items():
            print(f"{subject} - {marks}")


def add_marks():
    if len(subjects) == 0:
        print("No subjects available.")
        return

    subject = input("Enter subject: ").strip()

    if subject in subjects:
        marks = float(input("Enter marks: "))

        if marks >= 0 and marks <= 100:
            subjects[subject] = marks
            print("Marks added successfully!")
        else:
            print("Marks must be between 0 and 100.")
    else:
        print("Subject not found!")


def calculate_average():
    if len(subjects) == 0:
        print("No subjects available.")
        return

    total = 0

    for marks in subjects.values():
        total = total + marks

    average = total / len(subjects)

    print(f"Your average mark is: {average:.2f}")


def find_highest():
    if len(subjects) == 0:
        print("No subjects available.")
        return

    highest_subject = ""
    highest_mark = -1

    for subject, marks in subjects.items():
        if marks > highest_mark:
            highest_mark = marks
            highest_subject = subject

    print(f"Highest mark: {highest_subject} - {highest_mark}")


def find_lowest():
    if len(subjects) == 0:
        print("No subjects available.")
        return

    lowest_subject = ""
    lowest_mark = 101

    for subject, marks in subjects.items():
        if marks < lowest_mark:
            lowest_mark = marks
            lowest_subject = subject

    print(f"Lowest mark: {lowest_subject} - {lowest_mark}")


def search_subject():
    subject = input("Enter subject to search: ").strip()

    if subject in subjects:
        print(f"{subject} - {subjects[subject]}")
    else:
        print("Subject not found!")


def remove_subject():
    subject = input("Enter subject to remove: ").strip()

    if subject in subjects:
        del subjects[subject]
        print("Subject removed successfully!")
    else:
        print("Subject not found!")


while True:
    print("\n================================")
    print("       PERSONAL STUDY TRACKER")
    print("================================")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Add Marks")
    print("4. Calculate Average")
    print("5. Find Highest Mark")
    print("6. Find Lowest Mark")
    print("7. Search Subject")
    print("8. Remove Subject")
    print("9. Exit")
    print("================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_subject()

    elif choice == 2:
        view_subjects()

    elif choice == 3:
        add_marks()

    elif choice == 4:
        calculate_average()

    elif choice == 5:
        find_highest()

    elif choice == 6:
        find_lowest()

    elif choice == 7:
        search_subject()

    elif choice == 8:
        remove_subject()

    elif choice == 9:
        print("Thank you for using Personal Study Tracker! 👋")
        break

    else:
        print("Invalid choice! Please try again.")