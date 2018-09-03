#https://stackoverflow.com/questions/41445723/how-can-i-add-a-new-tab-to-an-existing-sheet-via-the-the-google-sheets-api


import gspread
import json
import pprint
import time
import re
from difflib import SequenceMatcher
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

def clear_file(file_name):
    file = open(file_name,'w')
    file.close()
    time.sleep(1)
if __name__ == '__main__':
    Today_Date = date.today().isoformat()
    # Today_Date = date.fromordinal(date.today().toordinal() - 1)
    # print Today_Date
    ##########################################################

    New_name_sheet = "CHR_UAT_WEEK_" + str(Today_Date)
    clear_file("Week_sheet_name.txt")
    open('Week_sheet_name.txt', 'w').write(New_name_sheet)

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) # get email and key from creds

    gfile = gspread.authorize(credentials) # authenticate with Google
    sheet = gfile.open("OM_Statistics_Error_Log").batch_update( {'requests':[{'addSheet':{'properties':{'title': New_name_sheet}} }]})
    sheet = gfile.open("OM_Statistics_Error_Log")
    sheet_CHR = sheet.worksheet(New_name_sheet)
    sheet_CHR.update_cell(1,2,"No")
    sheet_CHR.update_cell(1,3,"Module")
    sheet_CHR.update_cell(1,4,"Log filename")
    sheet_CHR.update_cell(1,5,"Date")
    sheet_CHR.update_cell(1,6,"Status")
    sheet_CHR.update_cell(1,7,"Assignee")
    sheet_CHR.update_cell(1,8,"Detail of log")
    sheet_CHR.update_cell(1,9,"DEV answer")
    sheet_CHR.update_cell(2,2,"1")
    sheet_CHR.update_cell(2, 3, "batch")
    sheet_CHR.update_cell(2, 4, "chr-error-logs-batch-2018-09-01_00.log")
    sheet_CHR.update_cell(2, 5, "18-09-01 00:15:40.706")
    sheet_CHR.update_cell(2, 6, "New")
    sheet_CHR.update_cell(2, 7, "TungNT")
    sheet_CHR.update_cell(2, 8, "WARN [org.springframework.scheduling.quartz.SchedulerFactoryBean#0_Worker-2 CustomerDiffer.diff:130][M]+CustomerConfigPo[id=705487169313047085,clusterId=0,companyId=1,accountId=0,customerId=16778480,configType=MYPAGE,configValue=JA,version=1,insertDatetime=Fri Aug 31 09:17:04 UTC 2018,updateDatetime=Fri Aug 31 09:17:04 UTC 2018]")




    ##########################################################


# sheet_CHR.update_cell(start_line, 2, content_sheet.__len__() + 1)
# sheet_CHR.update_cell(start_line, 3, list_content_update['NAME_APP'])
# sheet_CHR.update_cell(start_line, 4, list_content_update['LOG_FILE'].rstrip())
# sheet_CHR.update_cell(start_line, 5, list_content_update['DATE_TIME'])
# sheet_CHR.update_cell(start_line, 6, "New")
# sheet_CHR.update_cell(start_line, 7, "TungNT")
# sheet_CHR.update_cell(start_line, 8, list_content_update['DETAIL_LOG'].rstrip())

# sheet = gfile.open("OM_Statistics_Error_Log").batch_update({'requests':[{'addSheet':{'properties':{'title': 'CHR_UAT_2018_0903_to_0910'}} }]})
# sheet_CHR = sheet.worksheet("CHR_UAT_2018")
# content = sheet_CHR.get_all_records()
# string_1 = "WARN [service.cluster.scheduler-2 XHeartbeat.sweep:160]sweep key: 147235074, value: XMember[id=147235074,appId=17,appName=mailscheduler,processId=36162], retries: 1, timestamp: 2018-08-18 12:58:39.913"
# string_2 = "WARN [service.cluster.scheduler-2 XHeartbeat.sweep:160]sweep key: 717564545, value: XMember[id=717564545,appId=85,appName=ams.api.wallet,processId=35413], retries: 1, timestamp: 2018-08-18 12:58:42.925"
# pp = pprint.PrettyPrinter()
# pp.pprint(content.__len__())
# pp.pprint(content[0]['Detail of log'])
# pp.pprint(content)

# sheet_CHR.delete_row(104)

# score =  SequenceMatcher(None, string_1 , string_2).ratio()
# print(score)
# List_detail_log_sheet = []
# for i in range(0, content.__len__()):
#     List_detail_log_sheet.append(content[i]['Detail of log'])
#
# print List_detail_log_sheet
# if string_1 in List_detail_log_sheet:
#     start_row = content.__len__() + 2
#     sheet_CHR.update_cell(start_row,2,content.__len__() + 1)
#     sheet_CHR.update_cell(start_row, 3, "wallet")
#
# else:
#     print "NOT OK"
# pp.pprint(content[964])
# all_cells = sheet.acell('B966').value
#sheet.update_cell(968,2,"ERR [FX0000001343] portalweb=1B$B$G%(%i!<$,H/@8$7$^$7$?!#=1B(B2018-07-17 10= :49:50,203, [http-nio-8087-exec-20] ERROR phn.com.nts.util.common.CommonUti= l Failed to copy full contents from '/opt/tomcat_backend/webapps/amsadmin/o= pt/tomcat/upload/6104518_GBG_20180717104950_1.pdf' to '/opt/tomcat/upload/r= kt/6104518_GBG_20180717104950_1.pdf'(/opt/tomcat_backend/logs/rktbe.log)")
# print(all_cells)

# file handle fh
# Edit google sheet
# ====================================================

# start_row = content.__len__() + 3
# fh = open('key_4.txt')
# while True:
#     # read line
#     line = fh.readline()
#     sheet.update_cell(start_row,2,line)
#     start_row = start_row + 1
#     # in python 2, print line
#     # in python 3
#     # print(line)
#     # check if line is not empty
#     if not line:
#         break
# fh.close()
# ====================================================
# if 'wlau-portalweb01' in open('fill_content_message.txt').read():
#     first_line = "wlau-portalweb01"
#     with open('key_4.txt', 'r') as original: data = original.read()
#     with open('key_4.txt', 'w') as modified: modified.write(first_line + "\n" + data)
# if 'wlau-portalweb02' in open('fill_content_message.txt').read():
#     first_line = "wlau-portalweb02"
#     with open('key_4.txt', 'r') as original: data = original.read()
#     with open('key_4.txt', 'w') as modified: modified.write(first_line + "\n" + data)




# def update_message_send_to_sheet(new_content):
#     file = open("send_sheet.txt", "w")
#     file.close()
#     time.sleep(1)
#     file = open("send_sheet.txt", "w")
#     file.write(new_content)
#     file.close()
# def clear_file(file_name):
#     file = open(file_name,'w')
#     file.close()
#     time.sleep(1)


# if __name__ == '__main__':
    ################ Edit message content to file ##############################
    # clear_file("key.txt")
    # filter = open('fill_content_message.txt').read().splitlines()
    # parsing = False
    # for line in filter:
    #     if line.startswith("Message Text =1B$B!'=1B(B"):
    #         parsing = True
    #     elif line.startswith("=1B$BHw9M!'=1B(B"):
    #         parsing = False
    #     if parsing:
    #         with open("key.txt", 'a') as mykey:
    #             mykey.write(line)
    #             mykey.write("\n")
    #
    # with open('key.txt') as infile, open("key_2.txt",'w') as outfile:
    #     clear_file("key_2.txt")
    #     for line in infile:
    #         if not line.strip():
    #             continue
    #         outfile.write(line)
    #
    # with open('key_2.txt') as f, open("key_3.txt",'w') as outfile:
    #     clear_file("key_3.txt")
    #     outfile.write(" ".join(line.strip() for line in f))
    # file = open('key_3.txt','r+')
    # line = file.read()
    # if 'ERR' in line and 'WARN' not in line:
    #     print '\nERR [FX'.join(re.split('ERR\s\[FX', line))
    #
    # if 'ERR' not in line and 'WARN' in line:
    #     print '\n\nWARN [FX'.join(re.split('WARN\s\[FX', line))
    #
    # if 'ERR' in line and 'WARN' in line:
    #     print 'Message content include both "WARN" and "ERR", please paste from your email !!!'
    ################ Edit message content to file ##############################

    # with open('key_4.txt','w') as ufile:
    #     ufile.write('\n\nWARN [FX'.join(re.split('WARN\s\[FX', line)))

    # print '\nWARN [FX'.join(re.split('WARN\s\[FX', line))
    # Keyword "use re  python add new line before string"
    # https: // stackoverflow.com / questions / 45039268 / to - add - a - new - line - before - a - set - of - characters - in -a - line - using - python



    # List some error can have when setup
# https://github.com/burnash/gspread/issues/513
