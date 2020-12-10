from pathlib import Path
class Append:

    def append_file(self):
        name_of_file = (input("Please enter the name of your existing "
                              "file you would like to append text to: "))
        name_of_file = name_of_file + ".txt"
        my_file = Path(name_of_file)
        if my_file.exists():

            my_file = open(name_of_file, "a")
            file_input = (input("Please enter your input in your file: "))
            my_file.write("\n" + file_input)
            my_file.close()
        else:
            print("Error!\nThe file was not found")