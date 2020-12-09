from Add_to_dos import Add_to_dos
from Append import Append
from Read import Read
from datetime import date

todays_date = date.today()
print(f"Today's date: {todays_date}")
print("Welcome to your ToDos app \nPlease enter from the menu below")

continue_loop = True


def return_to_main():
    global continue_loop
    error_input = (input("Would you like to go back the menu: "
                         "Press [y] to go back \nOr any other characters to exit"))
    if error_input == "y" or "Y":
        continue_loop = True
    else:
        continue_loop = False
        exit(0)


while continue_loop:
    menu_input = int(input("[1] Add new ToDo file and add your text"
                           "\n[2] Append to an existing file\n""[3] Read from an existing file\n"))
    if menu_input == 1:
        to_do = Add_to_dos()
        to_do.add_file()
        return_to_main()
    elif menu_input == 2:
        append = Append()
        append.append_file()
        return_to_main()
    elif menu_input == 3:
        try:
            read = Read()
            read.read_file()
        except OSError as e:
            print("Error!\nThe file was not found")
        except:
            print("Error \n nr2")
        return_to_main()
    else:
        print("Error \nCould not find the menu choice in your input")
        return_to_main()
