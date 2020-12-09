class Add_to_dos():

    def add_file(self):
        name_of_file = (input("What would you like to name it?"))
        name_of_file = name_of_file + ".txt"

        my_file = open(name_of_file, "w+")
        file_input = (input("Please enter your input in your file: "))
        my_file.write(file_input)