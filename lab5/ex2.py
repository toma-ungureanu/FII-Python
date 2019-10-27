import os



def printBytes(path):
    file = open(path, "r")
    print(file.read(4096))
    file.close()


def printDirContents(path):
    print(os.listdir(path))


def main():
    try:
        path = input(" Enter the desired path: ")
        if os.path.isfile(path):
            statInfo = os.stat(path)
            if statInfo.st_size < 4096:
                raise EOFError
            printBytes(path)
        else:
            if os.path.isdir(path):
                printDirContents(path)
            else:
                raise OSError
    except UnicodeDecodeError:
        print(" Invalid file format!")
    except OSError:
        print(" Enter a valid path!")
    except EOFError:
        print(" File size is too small")


main()