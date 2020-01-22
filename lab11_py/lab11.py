import hashlib
import itertools
import os
import re
import time


def ex1(string):
    return string.split()


def ex2(regex_string, string, x):
    return [word for word in re.compile(regex_string).findall(string) if len(word) == x]


def ex3(string, regular_exp_list):
    string_list = list()
    for regular_exp in regular_exp_list:
        string_list.append(re.compile(regular_exp).findall(string))
    return list(set(itertools.chain(*string_list)))


def ex6(string):
    vocals = "aeiou"
    if str.lower(string[0]) in vocals and str.lower(string[-1]) in vocals:
        for index in range(len(string)):
            if index % 2 == 1:
                string = string[:index] + "*" + string[index + 1:]
    return string


def ex7(cnp_string):
    cnp_regex = r"([1-8])([0-9][0-9])((0[1-9])|10|11|12)(([0-2][1-9])|30|31)([0-9][1-9])([0-9][0-9][1-9])([0-9])"
    if re.compile(cnp_regex).fullmatch(cnp_string):
        return True
    else:
        return False


def ex8(dir_path, regex):
    flag1 = False
    flag2 = False
    regex_comp = re.compile(regex)
    for subdir, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(subdir, file)
            if regex_comp.search(full_path):
                flag1 = True
            fd = open(full_path, "r")
            lines = fd.read()
            if regex_comp.search(lines):
                flag2 = True
            if flag2 and flag1:
                print(">>", full_path)
            elif flag1 or flag2:
                print(full_path)
            fd.close()
            flag1 = False
            flag2 = False


# Write a function that receives a directory as argument and returns a list of dictionaries with
#     data about all the files in that directory. For each file, the following information will be
#     retrieved: file_name, md5 hash of file, sha256 hash of file, size_file (in bytes), time when
#     the file was created (human-readable) and the absolute path to the file.

def ex9(dir_path):
    dict_list = []
    file_dict = {}
    for subdir, dirs, files in os.walk(dir_path):
        for file in files:
            # get the name of the file
            file_dict["file_name"] = os.path.splitext(file)[0]

            # get the full path
            full_path = os.path.join(subdir, file)
            file_dict["full_path"] = full_path
            # st = os.stat(full_path)

            # get the size of the file
            file_dict["file_size"] = os.path.getsize(full_path)

            # get the creation time of the file
            file_dict["creation_time"] = "%s" % time.ctime(os.path.getctime(full_path))

            # get the hashes of the file
            with open(full_path, "rb") as f:
                file_md5_hash = hashlib.md5()
                file_sha256_hash = hashlib.sha256()
                while chunk := f.read(4096):  # python 3.8+
                    file_md5_hash.update(chunk)
                    file_sha256_hash.update(chunk)
                file_dict["file_hash_md5"] = file_md5_hash.hexdigest()
                file_dict["file_hash_sha256"] = file_sha256_hash.hexdigest()

            dict_list.append(file_dict)
            file_dict = {}
    return dict_list


def hashfile(path):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(65536)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(65536)
    afile.close()
    return hasher.hexdigest()


def ex10(dir_path):
    start_time = time.time()
    dups = {}
    for subdir, dirs, files in os.walk(dir_path):
        for file in files:
            path = os.path.join(dir_path, file)
            file_hash = hashfile(path)
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]

    dups_list = []
    for key in dups:
        if len(dups[key]) > 1:
            dups_list.append(dups[key])

    return dups_list, "%s seconds" % (time.time() - start_time)


re_list = [r"\b[a-z]*[0-9]+\b", r"\b[a-z]+[0-9]*\b"]
# print(ex6("America"))
# print(ex7("1850103274046"))
# ex8(r"C:\Users\thomi\Desktop\BD", "lab")
# print(ex9(r"C:\Users\thomi\Desktop\BD"))
print(ex10(r"C:\Users\thomi\Desktop\BD"))
# print(ex3("one1 one two three four five six seven eight nine ten 1 2 3 4 5 6 7 8 9 10 ", re_list))
# print(ex2(r"\b[a-z]*\b", "one two three four five six seven eight nine ten", 3))
