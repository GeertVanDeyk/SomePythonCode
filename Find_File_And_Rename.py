import os

def FindFileAndRename(the_path,change_from_this,change_into_that):
        os.chdir(str(the_path).replace('\\','/'))
        number_files_changed = 0
        number_of_files_in_directory = len(os.listdir(os.getcwd()))

        for file in os.listdir(os.getcwd()):
                original_filename = str(os.path.basename(file))
                if (original_filename.find(str(change_from_this)) != -1):
                        print('Renaming file : ' + original_filename)
                        os.rename(original_filename,original_filename.replace(str(change_from_this),str(change_into_that)))
                        number_files_changed += 1

        print(str(number_files_changed) + ' files changed of a total number of ' + str(number_of_files_in_directory) + " files in the directory")





if __name__ == '__main__':
        print('Starting ' + str(os.path.basename(__file__)) + ' in stand-alone mode.')
        mypath = str(input('Path to the folder you want to run the rename script in : ')).replace('\\','/')
        my_string_to_change = input('Which part of the file name you want to change? ')
        change_my_string_to = input('What do you want this part to be changed to? ')
        FindFileAndRename(mypath,my_string_to_change,change_my_string_to)
