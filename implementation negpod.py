def main_menu():
    print("1. Do you have frequent blackouts? ")
    print("2. Have you had any thoughts of suicide? ")
    print("3. Do you often have seizures?")
    print("4. Have you ever heard people talking about you when no one else is around?")
    print("5. Exit")
    selection = int(input(" Enter Question Number:"))
    if selection >= 4:
        print(r"Answer Yes\No :")
    elif selection == 5:
        main_menu()
    else:
        print("Try Again")
        main_menu()


main_menu()
