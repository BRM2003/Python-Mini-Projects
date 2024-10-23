from termcolor import cprint, colored
from hurry.filesize import size
from tabulate import tabulate
from pathlib import Path
import time
import sys
import os


class EditFile():
    FILENAME = 'file name'
    FILE_TYPE = 'file type'
    EXISTS = 'is exists'
    SIZE = 'size'
    CR_TIME = 'creation time'

    __file = {
        FILENAME: '',
        FILE_TYPE: '',
        EXISTS: False,
        SIZE: 0,
        CR_TIME: time.time()
    }
    
    def __init__(self, filepath):
        self.file = filepath

    def is_file_name(self, text):
        # Check if the string contains a dot and a file extension
        return '.' in text and len(text.split('.')[-1]) > 0


    @property
    def file(self):
        return self.__file

    @file.getter
    def filepath(self):
        return self.__file[self.FILENAME]

    @file.getter
    def filetype(self):
        return self.file[self.FILE_TYPE]

    @file.getter
    def filexists(self):
        return self.file[self.EXISTS]

    @file.setter
    def file(self, path):
        filename = str(path) if self.is_file_name(path) else str(path) + '.txt'
        file_type = filename.split('.')[-1].lower()
        f = Path(filename)

        self.__file = {
            self.FILENAME: f,
            self.FILE_TYPE: file_type,
            self.EXISTS: f.is_file(),
            self.SIZE: 'the File was not created' if not f.is_file() else f.stat().st_size,
            self.CR_TIME: 'the File was not created' if not f.is_file() else time.ctime(f.stat().st_ctime)
        }


    def error_msg(self, err_code=904):
        if err_code == 904:
            return "There is no such file: " + colored(text=self.filepath, attrs=['bold', 'reverse'])
        elif err_code == 909:
            return colored('You cannot delete this file!!!', 'white', 'on_red')


    def show(self):
        tab = []
        for element in self.file:
            el_value = size(self.file[element]) if element == self.SIZE and self.filexists else self.file[element]
            tab.append([element.title(), colored(el_value, 'light_yellow')])
        print(tabulate(tab, headers=['Name', 'Value']))

    def read(self):
        if not self.filexists:
            cprint(self.error_msg(), 'white', 'on_red')
            return Exception(self.error_msg())
        with open(self.filepath) as fl:
            print(fl.read())

    def write(self):
        if not self.filexists:
            if input(f"Would you like to create a new file {self.filepath}? (y/n): ").strip().lower() == 'n':
                cprint(self.error_msg(), 'white', 'on_red')
                return Exception(self.error_msg())
        try:
            with open(self.filepath, 'w') as f:
                print("Enter your text (type #SAVE# on a new line to save and exist):")
                text = input().rstrip()
                while not text.rstrip().endswith("#SAVE#"):
                    text += "\n" + input()
                f.write(text.rstrip()[:-6])
        except FileNotFoundError:
            cprint(self.error_msg(), 'white', 'on_red')

    def delete(self):
        if self.filetype == 'py':
            raise Exception(self.error_msg(909))
        if input(f"Would you like to create a new file {self.filepath}? (y/n): ").strip().lower() == 'y':
            os.remove(self.filepath) if self.filexists else cprint(self.error_msg(), 'white', 'on_red')
            cprint(f"{self.filepath} was successfully deleted!", 'green')
        


        
        


def main(filename='', command=''):

    def get_file_name():
        print("\nEnter the filename to open and edit or create a new one\nEnter 'exit' to close this programm\n")
        return input("Filename: ").strip()

    def get_command():
        print("""
    Enter the command for action
        1. Info
        2. Read
        3. Write
        4. Delete

    Enter 'exit' to close this programm
    """)
        while True:
            try:
                cmd = input("Command: ").strip().lower()
                if cmd.lower() == 'exit':
                    return cmd
                if 0 < int(cmd) < 5:
                    return cmd
                raise ValueError
            except ValueError as e:
                print('Invalid command!', str(e))


    filename = filename if filename else get_file_name()
    command = command if command else get_command()

    while filename.lower() != 'exit' and command.lower() != 'exit':
        file = EditFile(filename)
        if command in ('-i', 'show', '1'):
            file.show()
        elif command in ('-r', 'read', '2'):
            file.read()
        elif command in ('-w', 'write', '3'):
            file.write()
        elif command in ('-d', 'delete', '4'):
            file.delete()
        
        if command in ('-r', '-w', '-d', '-i'):
            break

        command = get_command()



if __name__ == "__main__":
    command = filename = ''
    arg = sys.argv
    if len(arg) > 1:
        if arg[1] in ('-i', '-w', '-d', '-s'):
            command = arg[1]
            if len(arg) > 2:
                filename = arg[2]
        else:
            filename = arg[1]
    main(filename=filename, command=command)