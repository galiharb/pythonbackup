import os
import datetime

masuk = 'cd /home/surat/ &&'

perintah = 'tar -zcvf '

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)

nama_file =  yesterday.strftime('%d-%b-%Y-esurat-code.tar.gz')
nama_filedb = yesterday.strftime('%d-%b-%Y-esurat-db.sql')
nama_backup = yesterday.strftime('%d-%b-%Y-backup-esurat.tar.gz')

nama_folder = ' public_html'
kompres = perintah+nama_file+nama_folder

os.system(masuk+kompres)
os.system('mv /home/surat/'+nama_file+' /root/galih/tempsurat/')
os.system('mysqldump --single-transaction -usurat -p3B8wt0PFyOL1HyTX surat > /root/galih/tempsurat/'+nama_filedb)

os.system('cd /root/galih/tempsurat/ && tar -zcvf '+nama_backup+' '+nama_file+' '+nama_filedb)
os.system('rm -f /root/galih/tempsurat/'+nama_file+' /root/galih/tempsurat/'+nama_filedb)

#pindah ke qnap
os.system('mv /root/galih/tempsurat/'+nama_backup+' /backupEsurat/')
os.system('rm -f /root/galih/tempsurat/'+nama_backup)

print ("selesai")