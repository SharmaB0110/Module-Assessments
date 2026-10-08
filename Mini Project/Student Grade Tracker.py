import csv

GRADES_FILE = "grades.csv"


def add_grades():
    """Get subject grades from the user and save them to a CSV file."""
    print("Enter subject grades. Type 'done' when finished.")

    while True:
        subject = input("Subject: ").strip()
        if subject.lower() == "done":
            break
        if not subject:
            print("Please enter a subject name.")
            continue

        try:
            grade = float(input("Grade: "))
        except ValueError:
            print("Please enter a numeric grade.")
            continue

        try:
            with open(GRADES_FILE, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([subject, grade])
            print("Grade saved.")
        except OSError as error:
            print(f"Could not save the grade: {error}")


def display_average():
    """Read saved grades and display their average."""
    grades = []

    try:
        with open(GRADES_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    grades.append(float(row[1]))
                except (IndexError, ValueError):
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("No grades file found yet. Add some grades first.")
        return
    except OSError as error:
        print(f"Could not read the grades file: {error}")
        return

    if not grades:
        print("There are no valid grades to average.")
        return

    average = sum(grades) / len(grades)
    print(f"Average grade: {average:.2f}")


def main():
    add_grades()
    display_average()


if __name__ == "__main__":
    main()