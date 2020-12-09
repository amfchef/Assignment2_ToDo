class Read:

    def read_file(self):
        name_of_file = (input("Please enter the name of your existing "
                              "file you would like to read from: "))
        name_of_file = name_of_file + ".txt"
        my_file = ""
        try:
            my_file = open(name_of_file, "r")
            print(my_file.read())
        except OSError as e:
            print("Error!\nThe file was not found")

        finally:
            my_file.close()