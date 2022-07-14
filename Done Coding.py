#!/usr/bin/python3 
Doctor=['General physician','psycologist','Neurologist']
print("E-HEALTH - MENTAL HEALTH(FIRST AID)")


def questions():
    print()
    print("QUESTIONS")
    print()
    print("1. Do you have frequent blackouts? ")
    print("2. Have you had any thoughts of suicide? ")
    print("3. Do you often have seizures?")
    print("4. Have you ever heard people talking about you when no one else is around?")
    print("5. Exit")
    print("")

    selection = int(input("Enter Question Number :"))
    option = str(input("Answer Yes or No : "))
    if selection > 5:
        print("Try again")
        print()
        questions()
    elif selection == 5:
        quit()
        print("Thank You")
        questions()
    if selection == 1:
        if option == "Yes":
            print(f"First Aid - Consult {doctors[0]}")
            print()
            questions()
        else:
            print("Try Again")
            print()
            questions()

    if selection == 2:
        if option == "Yes":
            print(f"First - Consult {doctors[1]}")
            print()
            questions()
        else:
            print("Try Again")
            print()
            questions()

    if selection == 3:
        if option == "Yes":
            print(f"First Aid - Consult  {doctors[2]}")
            print()
            questions()
        else:
            print("Try Again")
            print()
            questions()

    if selection == 4:
        if option == "Yes":
            print(f"First Aid - Consult  {doctors[2]}")
            print()
            questions()
        else:
            print("Try Again")
            print()
            questions()


questions()
