import sqlite3 

connection=sqlite3.connect("industry.db")
cursor=connection.cursor()

cursor.execute("create table industry (release_year integer, release_name text, year text)")

release_list= [
    (2004,"non-ferrous industry","Sydney"),
    (2005,"construction","Madrid"),
    (2007,"Technology","Vyana"),
    (2011,"Retail","Frankfurt"),
    (2014,"Consumer Services","Varwava")
]

cursor.executemany("insert into industry values (?,?,?)", release_list )

#print etmeliyik database rows-siralarini

for row in cursor.execute("select * from industry"):
    print(row)
connection.close()
