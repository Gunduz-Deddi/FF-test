
con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.execute('''create table stocks
(date text, trans text, symbol text,
 qty real, price real)''')
cur.execute("""insert into stocks
            values ('2006-01-05','BUY','RHAT',100,35.14)""")

con.commit()

cur.close()


#vacib kodlar sqlite with python