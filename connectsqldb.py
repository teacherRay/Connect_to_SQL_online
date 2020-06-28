import pymysql

#Set variables
room ='304i' #classroom
amp = 'am' #ampm
sid = 6291


#Setup hosted db example
conn = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12350280', passwd='7VEdsELCVz', db='sql12350280')
cur = conn.cursor()

#Update record example
cur.execute("""UPDATE ReportCardData SET PACo = 7, PACom = 9, PAHwk = 3, PAPart = 5, PABeh = 1 WHERE STUDENTID=%s""", (sid))

#Select record example using variables
#cur.execute("SELECT * FROM ReportCardData WHERE classroom = '104i' AND ampm = 'am'")
cur.execute("""SELECT * FROM ReportCardData WHERE classroom=%s AND ampm=%s""", (room,amp))
for r in cur:
    print(r)

#Close cursor and connections to db
cur.close()
conn.commit()
conn.close()

