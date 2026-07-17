from menu import main_menu
from database import start_work
from view_data import view_data


def main():

    while True:

        choice = main_menu()

        if choice == "1":
            start_work()

        elif choice == "2":
            view_data()

        elif choice == "3":
            print("\nThank You!")
            print("Exiting Vehicle Defect Tracking System...")
            break

        else:
            print("\nInvalid Choice! Please try again.")


if __name__ == "__main__":
    main()
