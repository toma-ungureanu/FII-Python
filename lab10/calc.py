import datetime
import sys

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])
result = 0
if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "/":
    result = a / b
elif operator == "%":
    result = a % b

timestamp = datetime.datetime.today().replace(microsecond=0)
string = ("%s %s + %s = %s" % (timestamp, a, b, result))

file = open(sys.argv[4], "w")
file.write(string)
file.close()
print(string)
