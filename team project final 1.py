
# Module 4 Team Project
# Course: CSS-225 Intro to Applied Programming
# Project Name: Menu Options Program
# Program Description:
# This program displays a menu with different learning options.
# The user can select an option by entering a number from 0 to 9.
# Each number represents a different activity or learning topic.
#this project is made my kaif,josue and milana
while True:
    print("\n===== Main Menu =====")
    print("1. Learn Python")
    print("2. Practice Programming")
    print("3. Study Cybersecurity")
    print("4. Learn Networking")
    print("5. Practice Linux")
    print("6. Study Databases")
    print("7. Learn Data Analytics")
    print("8. Review Algorithms")
    print("9. View Project Information")
    print("0. Exit")
    print("=====================")

    choice = input("Please enter your choice (0-9): ")

    if choice == "0":
        print("You entered " + choice + ". Thank you for using the program!")
        print("Program ended.")
        break

    elif choice == "1":
        print("You entered " + choice + ". You selected Learn Python.")

    elif choice == "2":
        print("You entered " + choice + ". You selected Practice Programming.")

    elif choice == "3":
        print("You entered " + choice + ". You selected Study Cybersecurity.")

    elif choice == "4":
        print("You entered " + choice + ". You selected Learn Networking.")

    elif choice == "5":
        print("You entered " + choice + ". You selected Practice Linux.")

    elif choice == "6":
        print("You entered " + choice + ". You selected Study Databases.")

    elif choice == "7":
        print("You entered " + choice + ". You selected Learn Data Analytics.")

    elif choice == "8":
        print("You entered " + choice + ". You selected Review Algorithms.")

    elif choice == "9":
        print("You entered " + choice + ". You selected Project Information.")

    else:
        print("You entered " + choice + ". Invalid choice. Please enter a number from 0 to 9.")

