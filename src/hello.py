#!/usr/bin/python3
# print ("Hello, Python!")
# print ("이장훈")
# print("AI프로그래밍")

# if True:
#     print ("True")

# else:
#     print ("False")

# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#     print ("False")

# if True:
#     print("나는")
#     print("바보다")
# else:
#     print("그런데")
#     print("바보와 천재는 종이 한장 차이다")

import sys

try:
    # open file stream
    file = open(file_name, "w")

except IOError:
    print("There was an error writing to", file_name)
    sys.exit()
print("Enter '", file_finish,)
print"' When finished"
while file_text != file_finish:
    file_text = raw_input("Enter text: ")
    if file_text == file_finish:
        # close the file
        file.close
        break
    file.write(file_text)
    file.write("\n")
file.close()

file_name = input("Enter filename: ")
if len(file_name) == 0:
    print("Next time please enter something")
    sys.exit()

try:
    file = open(file_name, "r")

except IOError:
    print ("There was an error reading file")
    sys.exit()
file_text = file.read()
file.close()
print (file_text)