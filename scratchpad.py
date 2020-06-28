UPDATE ReportCardData
SET column1 = value1, column2 = value2, ...
WHERE condition;


UPDATE CUSTOMERS
SET ADDRESS = 'Pune'
WHERE ID = 6;


cur.execute("SELECT Result FROM resultstable WHERE QuizID=? AND UserID=?", Quizno, UserID)
cur.execute("SELECT * FROM ReportCardData WHERE classroom =? AND ampm =?", classroom, classtime)