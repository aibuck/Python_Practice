from PyQt5.QtCore import QDateTime

datetime = QDateTime.currentDateTime()

print(datetime.toString())
print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))