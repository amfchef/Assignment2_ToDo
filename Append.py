class Append():

    def append_file(self):
        name_of_file = (input("Please enter the name of your existing "
                              "file you would like to append text to: "))
        name_of_file = name_of_file + ".txt"
        try:
            my_file = open(name_of_file, "a+")
            file_input = (input("Please enter your input in your file: "))
            my_file.write(file_input)
        except OSError as e:
            print("Error!\nThe file was not found")