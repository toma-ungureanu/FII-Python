import datetime
import sys


def problema1():
    d1 = sys.argv[1]
    date1 = datetime.datetime.strptime(d1, '%m/%d/%Y')
    d2 = sys.argv[2]
    date2 = datetime.datetime.strptime(d2, '%m/%d/%Y')
    return (date1 - date2).days


def problema2():
    date_list = list()
    date_str_list = list()

    date_1 = list()
    for i in range(1, len(sys.argv)):
        date = datetime.datetime.strptime(sys.argv[i], '%m/%d/%Y_%H.%M.%S')
        date_list.append(date)
        date_1.append(str(date))

    date_list.sort(reverse=True)
    date_str_list = [str(x) for x in date_list]

    diff = (date_list[0] - date_list[-1]).total_seconds()
    return date_str_list, diff

problema2()