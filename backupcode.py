import os
import datetime

PATH ="/home/webfolder/" #without public_html
TEMP ="/galih/tempwebapp/"
BACKUP = "/backupAPP/"

#### MYSQL #####
USER =""
PASSWORD =""
DATABASE =""
################

masuk = 'cd '+PATH+' &&'

perintah = 'tar -zcvf '

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)

nama_file =  yesterday.strftime('%d-%b-%Y-app-code.tar.gz')
nama_filedb = yesterday.strftime('%d-%b-%Y-app-db.sql')
nama_backup = yesterday.strftime('%d-%b-%Y-backup-app.tar.gz')

nama_folder = ' public_html'
kompres = perintah+nama_file+nama_folder

os.system(masuk+kompres)
os.system('mv '+PATH+' '+nama_file+' '+TEMP)
os.system('mysqldump --single-transaction -u'+USER+' -p'+PASSWORD+' '+DATABASE+' > 'TEMP+nama_filedb)

os.system('cd '+TEMP+' && tar -zcvf '+nama_backup+' '+nama_file+' '+nama_filedb)
os.system('rm -f 'TEMP+nama_file+' '+TEMP+nama_filedb)

#Move to backupfolder
os.system('mv 'TEMP+nama_backup+' '+BACKUP)
os.system('rm -f 'TEMP+nama_backup)

print ("selesai")
