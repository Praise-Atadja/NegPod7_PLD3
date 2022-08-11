"""our project is  an app that is capable of giving mental health support to people."""


print("************** WELCOME TO E-HEALTH ************")
print()
print("************ MENTAL HEALTH (FIRST AID) ************")
print()
print("E-Health can help you maintain and protect your mental"
      " health as well as help you get over mental stress.")
print("This app will benefit you by making it convenient to consult doctors and seek medical advice without fear of stigmatization.")
print("Using this app, you can speak with a physician, discuss your thoughts and concerns, and get the prescription the doctor has recommended.")

"""Functions Type1, Type2, Type3 and Type4 give information about specific doctors"""


def Type1():
    Doctor = "General Physician"
    Name = "Josh Mosh"
    Phone = +176648152364
    Location = "Paris, RK 846"
    print("Doctor: {}\nName: {}\nPhone: {}\nLocation: {}".format(
        Doctor, Name, Phone, Location))


def Type2():
    Doctor = "Psychologist"
    Name = "Junior Jeff"
    Phone = +250785298928
    Location = "Kigali, KG 255"
    print("Doctor: {}\nName: {}\nPhone: {}\nLocation: {}".format(
        Doctor, Name, Phone, Location))


def Type3():
    Doctor = "Neurologist"
    Name = "Kevin Hart"
    Phone = +146845465
    Location = "New York, NY 10030"
    print("Doctor: {}\nName: {}\nPhone: {}\nLocation: {}".format(
        Doctor, Name, Phone, Location))


def Type4():
    Doctor = "Psychiatrist"
    Name = "Hubert Prince"
    Phone = +256328836267
    Location = "Kampala, K1 4658"
    print("Doctor: {}\nName: {}\nPhone: {}\nLocation: {}".format(
        Doctor, Name, Phone, Location))


def questions():
    """Function displays a list of questions"""
    """This function allows the user to select different options."""
    print()
    print("PERSONAL DETAILS")
    print()
    str(input("Enter your name :"))
    str(input("Enter your gender(F/M) :"))
    int(input("Enter your age :"))
    float(input("Enter your height : "))
    float(input("Enter your weight :"))
    print()
    print("QUESTIONS")
    print()
    print("Please read through the following questions")
    print()
    print("1. Do you have frequent blackouts? ")
    print("2. Have you had any thoughts of suicide? ")
    print("3. Do you often have seizures?")
    print("4. Have you ever heard people talking about you when no one else is around?")
    print("5. Exit")
    print("")
    print("Please answer any question by typing in the question number.")
    print()

    def finish():
        done = input("Exit Yes/No: ")
        if done == "Yes":
            print()
            print("Thank you for using E-Health")
        if done == "No":
            print("Try Again")
            questions()

# If number selection is not found print Try Again else if selection is 5 print Thank You and exit
    selection = int(input("Enter Question Number : "))
    if selection > 5:
        print("Try again")
        questions()
    elif selection == 5:
        print("Thank You")
        quit()

    # If Answer is Yes for selection 1 the user is directed to a General Physician
    option = str(input("Answer Yes or No : "))
    if selection == 1:
        if option == "Yes":
            print()
            print(f'First Aid - Consult a physician')
            Type1()
            print()
            finish()

# If Answer is Yes for selection 2 the user is directed to a Psychologist
    if selection == 2:
        if option == "Yes":
            print()
            print(f'"First Aid - Consult a physician"')
            Type2()
            print()
            finish()
        else:
            print("Try Again")
            print()

    else:
        print()
        print("Try Again")
        questions()

    # If Answer is Yes for selection 3 the user is directed to a Neurologist
    if selection == 3:
        if option == "Yes":
            print()
            print(f'"First Aid - Consult a physician"')
            Type3()
            print()
            finish()
        else:
            print("Try Again")
            print()
            questions()


# If Answer is Yes for selection 4 the user is directed to a Psychiatrist
    if selection == 4:
        if option == "Yes":
            print()
            print(f'"First Aid - Consult a physician"')
            Type4()
            print()
            finish()
        else:
            print("Try Again")
            print()


questions()
