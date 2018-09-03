import re
import time
import gspread
import json
import pprint
import time
import re
import shutil
from datetime import date
import glob, os, os.path
from difflib import SequenceMatcher
from oauth2client.service_account import ServiceAccountCredentials


pattern1 = '====== HOST'

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

def delete_log_file():
    mydir = "C:\Users\OM-TRS\PycharmProjects\CHR_Update_Log_Sheet-master"
    filelist_remove_log = glob.glob(os.path.join(mydir, "*.log"))
    filelist_remove_csv = glob.glob(os.path.join(mydir, "*.csv"))
    for f in filelist_remove_log:
        os.remove(f)
    for f in filelist_remove_csv:
        os.remove(f)
####################### Function split log file to key file and value file##############################################
def split_log_to_file(log_file):
    clear_file("key_dic.txt")
    clear_file("value_dic.txt")
    with open(log_file, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]

            if line.startswith(pattern1):
                # print line
                update_key_dic(line)
                next_line = lines[i + 1]  # you may want to check that i < len(lines)
                #     print ' nextLine ', next_line, '\n'
                # print next_line
                update_value_dic(next_line)
# clear key file and value file before update new log


            # break
# https://stackoverflow.com/questions/6213063/python-read-next
# Get Next line OK

####################### Function split log file to key file and value file #############################################



##################### Process key file and value file export dictionary ################################################
def gen_dic():
    MyList = []
    clear_file("format_six_equal.txt")
    clear_file("format_five_equal.txt")
    clear_file("format_dashed.txt")
    str = open('key_dic.txt').read()
    del_1 = re.sub("====== ", "", str)
    open('format_six_equal.txt', 'w').write(del_1)
    str1 = open('format_six_equal.txt').read()
    del_2 = re.sub(" =====", "", str1)
    open('format_five_equal.txt', 'w').write(del_2)
    str3 = open('format_five_equal.txt').read()
    del_3 = re.sub(" - ", ":", str3)
    open("format_dashed.txt", 'w').write(del_3)

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
    return MyList
##################### Process key file and value file export dictionary ################################################
def get_duplicate_item_in_List(My_List_ERROR):
    Full_list = []
    Dup_List = []
    for i in range(0, My_List_ERROR.__len__()):
        for j in range(i+1, My_List_ERROR.__len__()):
            score =  SequenceMatcher(None, My_List_ERROR[i]['DETAIL_LOG'] , My_List_ERROR[j]['DETAIL_LOG']).ratio()
            if score > 0.6 :
                Dup_List.append(j)
    for i in range(0, My_List_ERROR.__len__()):
        Full_list.append(i)

    item_list = Full_list
    Res_list = []
    for e in Full_list:
        if e not in list(set(Dup_List)):
            Res_list.append(e)
# https://stackoverflow.com/questions/35731289/function-to-remove-duplicates-from-a-list-python?lq=1
# https://stackoverflow.com/questions/16603282/how-to-compare-each-item-in-a-list-with-the-rest-only-once
    return Res_list

# def delete_duplicate_item_in_List(Duplicate_List,Full_List):
#
#     new_list = []
#     for item  in Full_List:
#         if e not in ('item', 5):
#             new_list.append(e)
#     item_list = new_list


#################### Get Detail Log from sheet to Compare ##############################################################
def get_sheet_detail_log(name_sheet):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)  # get email and key from creds

    gfile = gspread.authorize(credentials)  # authenticate with Google

    sheet = gfile.open("OM_Statistics_Error_Log")
    sheet_CHR = sheet.worksheet(name_sheet)
    content = sheet_CHR.get_all_records()
    # string_1 = "WARN [service.cluster.scheduler-2 AbstractServiceCluster.ping:267][service.cluster]failed to ping, member: XMember[id=8955265,appId=1,appName=server,processId=4427], service: AbstractServiceImporter.XServiceImpl[id=693682773730263041,bus=8955265,type=system.config.server,domain=CONFIG], cause: service: CONFIG.system.config.server"
    pp = pprint.PrettyPrinter()
    # pp.pprint(content.__len__())
    # pp.pprint(content[0]['Detail of log'])
    # pp.pprint(content)
    List_detail_log_sheet = []
    for i in range(0, content.__len__()):
        List_detail_log_sheet.append(content[i]['Detail of log'])

    return List_detail_log_sheet



def update_sheet(list_content_update,name_sheet):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)  # get email and key from creds

    gfile = gspread.authorize(credentials)  # authenticate with Google

    sheet = gfile.open("OM_Statistics_Error_Log")
    sheet_CHR = sheet.worksheet(name_sheet)
    content_sheet = sheet_CHR.get_all_records()
    start_line = content_sheet.__len__() + 2
    sheet_CHR.update_cell(start_line,2,content_sheet.__len__() + 1)
    sheet_CHR.update_cell(start_line,3,list_content_update['NAME_APP'])
    sheet_CHR.update_cell(start_line, 4, list_content_update['LOG_FILE'].rstrip())
    sheet_CHR.update_cell(start_line, 5, list_content_update['DATE_TIME'])
    sheet_CHR.update_cell(start_line, 6, "New")
    sheet_CHR.update_cell(start_line, 7, "TungNT")
    sheet_CHR.update_cell(start_line, 8, list_content_update['DETAIL_LOG'].rstrip())


def get_duplicate_item():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)  # get email and key from creds

    gfile = gspread.authorize(credentials)  # authenticate with Google

    sheet = gfile.open("OM_Statistics_Error_Log")
    sheet_CHR = sheet.worksheet("CHR_UAT_2018")
    content_sheet = sheet_CHR.get_all_records()
    list_index_dulice = []
    for i in range(0, content_sheet.__len__()):
        for j in range(i+1, content_sheet.__len__()):
            score =  SequenceMatcher(None, content_sheet[i]['Detail of log'] , content_sheet[j]['Detail of log']).ratio()
            if score > 0.6 :
                list_index_dulice.append(j)
    return list(set(list_index_dulice))

def delete_item_duplicate(d_list):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)  # get email and key from creds

    gfile = gspread.authorize(credentials)  # authenticate with Google

    sheet = gfile.open("OM_Statistics_Error_Log")
    sheet_CHR = sheet.worksheet("CHR_UAT_2018")
    content_sheet = sheet_CHR.get_all_records()
    sheet_CHR.delete_row(d_list[0])

#################### Function copy today file from 10.1.1.45 to local ##############################
def get_string_today():
    Today_Date = date.today().isoformat()
    return str(Today_Date)


def get_all_file_from_server():
    List_all_file = os.listdir('\\\\10.1.1.45\public\CHR_LOG\UATVN')
    return List_all_file

def get_all_file_today_from_server():
    string_today = get_string_today()
    extend_file = "csv"
    list_all_file = get_all_file_from_server()
    list_all_file_modify_today = []
    for i in range(0,list_all_file.__len__()):
        if string_today in list_all_file[i] and extend_file not in list_all_file[i]:
            list_all_file_modify_today.append(list_all_file[i])

    return list_all_file_modify_today


def copy_today_file_from_server_to_local():
    src_path = "\\\\10.1.1.45\public\CHR_LOG\UATVN\\"
    des_path = "C:\Users\OM-TRS\PycharmProjects\CHR_Update_Log_Sheet-master"
    list_file_need_copy_today = get_all_file_today_from_server()
    for i in range(0,list_file_need_copy_today.__len__()):
        shutil.copy2((src_path + str(list_file_need_copy_today[i])) , des_path)  # complete target filename given

def list_all_log_file_local():
    list_log_file = glob.glob("*.log")
    return list_log_file

if __name__ == '__main__':
    copy_today_file_from_server_to_local()
    ################################################
    nameWeekSheet = open("Week_sheet_name.txt").read()
    log_file_path = list_all_log_file_local()
    # print log_file_path

    for i in range(0, log_file_path.__len__()):
        split_log_to_file(log_file_path[i])
        List_Error = gen_dic()
        Rest_list = get_duplicate_item_in_List(List_Error)
        print Rest_list
        # print List_Error[List_Error.__len__() - 1]['DETAIL_LOG']
        List_Error_Sheet = get_sheet_detail_log(str(nameWeekSheet))
        # print str(List_Error_Sheet[List_Error_Sheet.__len__() - 2])
        # if List_Error[List_Error.__len__() - 1]['DETAIL_LOG'].rstrip() == List_Error_Sheet[List_Error_Sheet.__len__() - 2]:
        #     print 'OK'
        # else:
        #     print "NOT OK"
        for i in range(0, Rest_list.__len__()):
            if List_Error[Rest_list[i]]['DETAIL_LOG'].rstrip() not in List_Error_Sheet:
                update_sheet(List_Error[Rest_list[i]],str(nameWeekSheet))
                List_Error_Sheet = get_sheet_detail_log(str(nameWeekSheet))
            else:
                print "This log was exist !"



    delete_log_file()
    ################################################
    # delete from sheet FAIL #######################################
    # List_item_duplicate = get_duplicate_item()
    # while List_item_duplicate.__len__() > 0:
    #     print List_item_duplicate
    #     delete_item_duplicate(List_item_duplicate)
    #     List_item_duplicate = get_duplicate_item()
    # delete from sheet FAIL #######################################
    # E_list = gen_dic()
    # reduce_list = get_duplicate_item_in_List(E_list)
    # for i in range(0, reduce_list.__len__()):
    #     print E_list[reduce_list[i]]['DETAIL_LOG']




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
