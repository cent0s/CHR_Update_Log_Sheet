import re
import time
def clear_file(file_name):
    file = open(file_name,'w')
    file.close()
    time.sleep(1)


clear_file("format_six_equal.txt")
clear_file("format_five_equal.txt")
clear_file("format_dashed.txt")
str = open('key_dic.txt').read()
del_1 = re.sub("====== ","",str)
open('format_six_equal.txt', 'w').write(del_1)
str1 = open('format_six_equal.txt').read()
del_2 = re.sub(" =====", "", str1)
open('format_five_equal.txt','w').write(del_2)
str3 = open('format_five_equal.txt').read()
del_3 = re.sub(" - ", ":",str3)
open("format_dashed.txt",'w').write(del_3)


# def gettime_string(filename):
#     with open(filename, 'r') as f:
#
#         texts = f.readlines()
#         for i in range(0, len(texts)):
#             text = texts[i]
#             print text[:21]
#             print text[22:]
#
#
# gettime_string("value_dic.txt")
















# logfile = open("format_dashed.txt", "r")
# for line in logfile:
#     # if "WARN" in line:
#     #     line_split = line.split('WARN')
#     #     print line_split
#     # if "ERROR" in line:
#     #     line_split = line.split('ERROR')
#     line_split = line.split(": ")
#     # list = line_split[0], line_split[1]
#     list = line_split[0], line_split[1], line_split[2], line_split[3], line_split[4], line_split[5]

#  OK add to Mylist
MyList = []
with open("format_dashed.txt", 'r+') as f, open("value_dic.txt") as value_file:
    lines = f.readlines()
    time_contents = value_file.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        time_content = time_contents[i]
        line_split = line.split(": ")
        # MyList[i]['HOST'] = line_split[1]
        # MyList[i]['APP_NAME'] = line_split[3]
        # MyList[i]['FILELOG'] = line_split[5]
        # print line_split
        dict = {}
        dict['HOST'] = line_split[1]
        dict['NAME_APP'] = line_split[3]
        dict['LOG_FILE'] = line_split[5]
        dict['DATE_TIME'] = time_content[:21]
        dict['DETAIL_LOG'] = time_content[22:]
        MyList.append(dict)

#  OK add to Mylist

print MyList[2]