import os


def writePaths(dirname,filename):
    file_to_write = open(filename, "w+", encoding='utf-8')
    for root, dirs, files in os.walk(dirname):
        path = root.split(os.sep)
        file_to_write.write((len(path) - 1) * '---')
        file_to_write.write(os.path.basename(root))
        file_to_write.write("\n")
        for file in files:
            file_to_write.write(len(path) * '---')
            file_to_write.write(os.path.basename(file))
            file_to_write.write("\n")


def main():
    try:
        path = input(" Enter the desired path: ")
        file_to_write_in = input(" Enter the file you want to write in: ")
        if not os.path.isdir(path):
            raise OSError
        writePaths(path, file_to_write_in)
    except OSError:
        print(" Enter a directory!")


main()
