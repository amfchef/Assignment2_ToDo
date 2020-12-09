class Add_to_dos:

    def add_file(self):
        try:
            name_of_file = (input("What would you like to name it? "))
            name_of_file = name_of_file + ".txt"

            my_file = open(name_of_file, "w+")
            file_input = (input("Please enter your input in your file: "))
            my_file.write(file_input)
        except:
            print("Error\nSomething wrong happend")
        finally:
            my_file.close()