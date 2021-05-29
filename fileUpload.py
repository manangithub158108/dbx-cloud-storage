# importing the modules
import dropbox;

# creating the class
class fileUpload:
    def __init__(self, key, file_to, file_from):
        self.key = key;
        self.file_to = file_to;
        self.file_from = file_from;

        # initializng the dropbox
        dbx = dropbox.Dropbox(self.key);

        # uploading the files into the dropbox
        with open(self.file_to, 'rb') as f:
            dbx.files_upload(f.read(), file_from);

# creating a main function
def main():

    # definig the params
    file_to = input('Enter the file name >> ');
    file_from = "/trialFiles/" + file_to;
    key = "jYr8t6ZxTCIAAAAAAAAAAc5VgENQ8-S6FVwSa3SSBmR5SY5l-100SuNw56DIHTDi"

    # definig the class
    dbx = fileUpload(key, file_to, file_from);

    # writing the print statement
    print('File uploaded successfully');

# defining the function
main();


