import re
import time
import glob
import glob, os, os.path
from datetime import date, timedelta
import shutil

# conn = SMBConnection('salead',
#                      'repo@2k12',
#                      '192.168.14.1',
#                      'SERVER',
#                      use_ntlm_v2 = True)
# assert conn.connect('192.168.1.41', 139)
# with open('local_file', 'wb') as fp:
#     conn.retrieveFile('share', '/path/to/remote_file', fp)
def get_string_today():
    Today_Date = date.today().isoformat()
    yesterday = date.fromordinal(date.today().toordinal()-1)
    print Today_Date
    return Today_Date


def delete_log_file():
    mydir = "\\10.1.1.45\public\CHR_LOG\UATVN"
    filelist_remove = glob.glob(os.path.join(mydir, "*.csv"))
    for f in filelist_remove:
        os.remove(f)
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
        shutil.copy2(src_path + str(list_file_need_copy_today[i]) , des_path)  # complete target filename given
def list_all_log_fil_local():
    list_log_file = glob.glob("*.log")
    return list_log_file


if __name__ == '__main__':
    # List_File_Log = glob.glob("\\10.1.1.45\public\CHR_LOG\UATVN\*.csv")
    # copy_today_file_from_server_to_local()
    abc = list_all_log_fil_local()
    print abc


    # delete_log_file()
    # print(glob.glob("*.log"))
    # for i in range(0, log_file_path.__len__()):
    #     print log_file_path[i]
    #     print i
    #     print log_file_path.__len__()