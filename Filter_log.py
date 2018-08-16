import re
import time
import re

log_file_path = r"chr-error-logs-2018-08-13_11.log"
pattern1 = '====== HOST'
pattern2 = 'WARN'
pattern3 = 'ERROR'

def update_key_dic(key):
    with open("key_dic.txt", "a") as myfile:
        myfile.write(key)


def update_value_dic(value):
    with open("value_dic.txt", "a") as myfile:
        myfile.write(value)



def clear_file(file_name):
    file = open(file_name,'w')
    file.close()
    time.sleep(1)



with open(log_file_path, 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]

        if line.startswith(pattern1):
            print line
            update_key_dic(line)
            next_line = lines[i + 1]  # you may want to check that i < len(lines)
        #     print ' nextLine ', next_line, '\n'
            print next_line
            update_value_dic(next_line)
            # break
# https://stackoverflow.com/questions/6213063/python-read-next
# Get Next line OK





# string = open('key_dic.txt').read()
# new_str = re.sub("======"," ",string)
# open('format.txt', 'w').write(new_str)




# e_path, "r") as file:
#     for line in file:
#         if pattern1 in line and pattern2 or pattern3 in line + 1:
#             print line
#             print line + 1
# with open(log_file_path, 'r') as f:
#     for line in f:
#         if line.startswith(pattern1):
#             print line
#         #     update_key_dic(line)
#         # if line.startswith(pattern1):
#             print f.next()
#             update_value_dic()
            # update_value_dic(f.next())
            # Or use next(f, '') to return <empty string> instead of raising a
            # StopIteration if the last line is also a match.

# fh = open(log_file_path)
# while True:
#     # read line
#     line = fh.readline()
#     if line.startswith(pattern1):
#         print line
#         # update_key_dic(line)
#         print fh.next()
#     # in python 2, print line
#     # in python 3
#     # print(line)
#     # check if line is not empty
#     if not line:
#         break
# # fh.close()
