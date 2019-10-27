import os
import getpass
import platform
import multiprocessing


def main():
    if "2." in platform.python_version():
        print("=== Python 2 ===")
    else:
        if "3." in platform.python_version():
            print("=== Python 3 ===")
    print(getpass.getuser())
    print(os.path.abspath(__file__))
    print(os.path.basename(os.path.abspath(".")))
    print(platform.system())
    print(multiprocessing.cpu_count())


main()
