print("E-HEALTH - MENTAL HEALTH (FIRSTAID)")


def questions():

    print()
    print("QUESTIONS")
    print()
    print("1. Do you have frequent blackouts? ")
    print("2. Have you had any thoughts of suicide? ")
    print("3. Do you often have seizures?")
    print("4. Have you ever heard people talking about you when no one else is around?")
    print("5. Exit")
    selection = int(print("Enter Question Number :"))

    if selection > 5:
        input("answer")



    elif 1 and "No":
        print("Try Again")
    if selection == 2 and "Yes":
        print("First Aid - Contact Psychologist")
        print(" ")
        questions()
    elif selection == 3 and "Yes":
        print("First Aid - Contact Neurologist")
        print(" ")
        questions()
    elif selection == 4 and "Yes":
        print("First Aid - Contact Psychiatrist")
        print(" ")
        questions()
    else:
        print("Try Again")


questions()


