import sqlite3 

connection=sqlite3.connect("industry.db")
cursor=connection.cursor()

("create table industry (release_year integer, release_name text, release_city text)")

# buraxilish il,ad,seher
release_list= [
    (2004,"non-ferrous industry","Sydney city"),
    (2005,"construction","Madrid city"),
    (2007,"Technology","Vyana city"),
    (2011,"Retail","Frankfurt city"),
    (2014,"Consumer Services","Varwava city")
]

cursor.executemany("insert into industry values (?,?,?)", release_list )

#print etmeliyik database rows-siralarini

for row in cursor.execute("select * from industry"):
    print(row)
print("**************")  

cursor.execute("select * from industry where city=:c", {"c": "Frankfurt"})
industry_search = cursor.fetchall()
print(industry_search)

connection.close()



