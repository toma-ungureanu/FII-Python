import os


class Error(Exception):
    """Exception"""
    pass


class EmptyPathError(Error):
    """Raised when the input value is negative"""
    pass


def printDirTree(filename):
    for name in os.listdir(filename):
        path = os.path.join(filename, name)
        if os.path.isdir(path):
            print(os.path.abspath(path))
            os.chdir(path)
            printDirTree(path)


def main():
    try:
        path = input(" Enter the desired path: ")
        if not path:
            raise EmptyPathError
        if not os.path.isdir(path):
            raise OSError
        printDirTree(path)
    except OSError:
        print(" Enter a directory too look in!")
    except EmptyPathError:
        print(" Enter a path!")


main()