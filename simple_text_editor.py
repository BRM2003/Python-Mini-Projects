from pathlib import Path


class EditFile():
    PATH = 'path'
    FILE_TYPE = 'file_type'
    EXISTS = 'is_exists'

    __file = {
        PATH: '',
        FILE_TYPE: '',
        EXISTS: False
    }
    
    def __init__(self, filepath):
        self.file = filepath

    def is_file_name(self, text):
        # Check if the string contains a dot and a file extension
        return '.' in text and len(text.split('.')[-1]) > 0

    @property
    def file(self):
        return self.__file
    
    @file.setter
    def file(self, path):
        filename = str(path) if self.is_file_name(path) else str(path) + '.txt'
        file_type = filename.split('.')[-1].lower()
        self.__file = {
            self.PATH: Path(filename),
            self.FILE_TYPE: file_type,
            self.EXISTS: Path(filename).is_file()
        }
    
    def show(self):
        print(self.file)

    def read(self):
        # if not self.file[self.EXISTS]:
            # if 
        with open(self.file[self.PATH]) as fl:
            print(fl.read())

        
        




print("\nEnter the filename to open and edit or create a new one\nEnter 'exit' to close this programm\n")
while True:
    file = input("Filename: ")

    if file.lower() == 'exit':
        break

    EditFile(file).show()
    EditFile(file).read()

