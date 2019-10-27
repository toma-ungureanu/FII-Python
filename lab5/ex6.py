import os


class Error(Exception):
    """Exception"""
    pass


class EmptyPathError(Error):
    """Raised when the input value is negative"""
    pass


def copy_file(sourceFile, destDirectory, bytes_no):
    try:
        source_fd = open(sourceFile, "r", encoding='utf-8')
        buffer = source_fd.read(bytes_no)
        source_fd.close()
        dest_path = str(destDirectory + os.sep + os.path.basename(sourceFile))
        dest_fd = open(dest_path, "w+", encoding='utf-8')
        dest_fd.write(buffer)
        dest_fd.close()
    except ValueError:
        print(" Extension not supported")


def main():
    try:
        file_to_write_in = input(" Enter the absolute path of the file you want to copy: ")
        if not file_to_write_in:
            raise EmptyPathError

        directory_to_write_in = input(" Enter the directory in which you want to copy the file: ")
        if not directory_to_write_in:
            raise EmptyPathError

        bytes_to_copy = input(" Enter the number of bytes you want to copy: ")
        if not int(bytes_to_copy):
            raise ValueError

        copy_file(file_to_write_in, directory_to_write_in, int(bytes_to_copy))
    except EmptyPathError:
        print(" Enter a valid path!")
    except ValueError:
        print(" Enter an integer!")


main()
