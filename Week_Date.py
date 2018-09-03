from datetime import date

Today_Date = date.today().isoformat()
print 'Today is :', str(Today_Date)
str = open('Week_sheet_name.txt').read()
print str

