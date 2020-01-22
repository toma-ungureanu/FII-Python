import os
import struct
from os import access, R_OK, W_OK


class Error(Exception):
    """Exception"""
    pass


class EmptyPathError(Error):
    """Raised when the input value is negative"""
    pass


def search_by_content(target, to_search):
    pass


def get_file_info(path):
    dictionar = dict()
    st = os.stat(path)
    dictionar["full_path"] = os.path.abspath(path)
    dictionar["file_size"] = st.st_size
    name, dictionar["file_ext"] = os.path.splitext(path)
    if access(path, R_OK):
        dictionar["can_read"] = True
    else:
        dictionar["can_read"] = False

    if access(path, W_OK):
        dictionar["can_write"] = True
    else:
        dictionar["can_write"] = False
    return dictionar


def write_environ(path):
    file = open(path, "w+")
    file.write(str({item: os.environ[item] for item in os.environ}))


def recurse_browse(filename):
    for name in os.listdir(filename):
        actual_path = os.path.join(filename, name)
        if os.path.isdir(actual_path):
            print("DIR: ")
            print(os.path.abspath(actual_path))
            recurse_browse(actual_path)
        elif os.path.isfile(actual_path):
            print("FILE: ", end="")
            print(os.path.abspath(actual_path))
        else:
            print("UNKNOWN: ", end="")
            print(os.path.abspath(actual_path))


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


def pretty_function():
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


def get_size(dir_path='.'):
    total_size = 0
    dir_list = []
    file_list = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for dirname in dirnames:
            dir_list.append(os.path.abspath(dirname))
        for f in filenames:
            file_list.append(os.path.relpath(f))
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size, dir_list, file_list


def dir_dict(dir_path):
    dictionar = dict()
    dictionar["full_path"] = print(os.path.abspath(dir_path))
    dictionar["total_size"], dictionar["dir_list"], dictionar["file_list"] = get_size(dir_path)
    return dictionar


# 7. Write a function that parses a given archive and extracts the files with a certain extension.
#
# The function will have two parameters - container_path (a string representing the path of the container) and extension (a string representing the extension we are looking for).
#
# The container has the following format:
#
# - Starts with the string "CONTAINER"
#
# - The following byte represents the number of files in the archive
#
# - After the previously mentioned byte, for each file there will be
#
#     -> 4 - unsigned integer, little endian bytes representing the size.
#
#     -> 50 bytes representing the file name. (if the name has less than 50 characters, it will be padded with whitespaces)
#
#     -> The body of the file

def extract(file_path, extension):
    file = open(file_path, "rb")
    title = file.read(9)
    if title.decode() != "CONTAINER":
        return False

    files_count = ord(file.read(1))
    for i in range(files_count):
        little_size = file.read(4)
        file_name = file.read(50).decode().strip()
        size = struct.unpack('<I', little_size)
        if os.path.splitext(file_name)[-1] == extension:
            new_file = open(file_name, "wb")
            new_file.write(file.read(size[0]))
            new_file.close()
        else:
            file.seek(size[0] + file.tell())


extract("arhiva.container", ".exe")
# print(dir_dict(r"C:\Users\thomi\PycharmProjects\lab8"))
# print(recurse_browse(r"C:\Users\thomi\PycharmProjects\lab8"))
# pretty_function()
