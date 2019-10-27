import os


def printEnviron(path):
    file = open(path, "w+")
    file.write(str(os.environ))


def main():
    try:
        path = input(" Enter the desired path: ")
        printEnviron(path)

    except PermissionError:
        printEnviron(" File is not writable!")


main()
