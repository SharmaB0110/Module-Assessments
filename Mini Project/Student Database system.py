class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average grade: {self.average_grade():.2f}")


def main():
    students = []

    while True:
        print("\nStudent Database")
        print("1. Add a student")
        print("2. Display all students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter the student's name: ")

            try:
                age = int(input("Enter the student's age: "))
                grades_text = input(
                    "Enter grades separated by commas (for example, 85, 90, 78): "
                )
                grades = [float(grade.strip()) for grade in grades_text.split(",")]

                student = Student(name, age, grades)
                students.append(student)
                print(f"{name} was added to the database.")

            except ValueError:
                print("Please enter a valid age and numeric grades.")

        elif choice == "2":
            if not students:
                print("The database is empty.")
            else:
                for student in students:
                    print("\n--- Student Information ---")
                    student.display_info()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please choose 1, 2, or 3.")


main()