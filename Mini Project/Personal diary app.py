from datetime import datetime

DIARY_FILE = "diary.txt"


def add_entry():
    entry = input("Write your diary entry: ")

    try:
        with open(DIARY_FILE, "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n[{timestamp}]\n{entry}\n")
        print("Entry saved.")
    except PermissionError:
        print("Error: You don't have permission to write to the diary file.")
    except OSError as error:
        print(f"Error saving the entry: {error}")


def view_entries():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as file:
            contents = file.read()
            if contents:
                print("\n--- Previous Diary Entries ---")
                print(contents)
            else:
                print("Your diary has no entries yet.")
    except FileNotFoundError:
        print("No diary file found yet. Add an entry first.")
    except PermissionError:
        print("Error: You don't have permission to read the diary file.")
    except OSError as error:
        print(f"Error reading the diary: {error}")


def main():
    while True:
        print("\n1. Add an entry")
        print("2. View entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Please enter 1, 2, or 3.")


main()