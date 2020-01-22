import os
import re


def problema1(path):
    ip_regex = r"^(?=.*[^\.]$)((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.?){4}"
    ip_list = []
    compiled_re = re.compile(ip_regex)
    if os.path.isfile(os.path.abspath(path)) and str.find(os.path.abspath(path), "access.log"):
        fd = open(path, "r")
        line = fd.readline()
        while line:
            ip_list.append(compiled_re.search(line).group())
            line = fd.readline()

    elif os.path.isdir(os.path.abspath(path)):
        for subdir, dirs, files in os.walk(path):
            for file in files:
                if os.path.isfile(os.path.abspath(path)) and str.find(os.path.abspath(path), "access.log"):
                    full_file_path = os.path.join(path, file)
                    fd = open(full_file_path, "r")
                    line = fd.readline()
                    while line:
                        ip_list.append(compiled_re.search(line).group())
                        line = fd.readline()

    freq = dict()
    for item in set(ip_list):
        freq[item] = ip_list.count(item)

    return [x[0] for x in sorted(freq.items(), reverse=True)][:7]


def problema2():
    pass


problema1("ips.txt")
