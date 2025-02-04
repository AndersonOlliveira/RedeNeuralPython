from ftplib import FTP

ftp = FTP("ftp.ncdc.noaa.gov")
ftp.login()
ftp.cwd("pub/data/noaa/1901")
files = ftp.nlst()
for f in files:
    with open(f,"wb") as arqLocal:
        ftp.retrbinary("RETR "+f, arqLocal.write)
ftp.quit()
