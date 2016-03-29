import urllib
from bs4 import BeautifulSoup
import sqlite3
text=open("a.txt","w+")
conn = sqlite3.connect('redmi3.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Counts;

CREATE TABLE Counts (
	id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    review   TEXT UNIQUE)
''')

i=1;
j=2
while True:	
	nameList=list()
	link="http://www.amazon.in/product-reviews/B018U7PG30/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&showViewpoints=1&sortBy=recent&pageNumber="+str(j)
	
	html = urllib.urlopen(link)
	bsObj = BeautifulSoup(html.read())
	nameList = bsObj.findAll("", {"class":"a-size-base review-text"})
	for name in nameList:
		text.write(str(i))
		text.write(" ")
		name1=name.get_text()
		name2=" "
		try:
			text.write(name1)
			
		except:
			text.write(name2)
		cur.execute('''INSERT OR IGNORE INTO Counts (review) 
        VALUES ( ? )''', ("NULL", ))
		cur.execute('''INSERT OR IGNORE INTO Counts (review) 
        VALUES ( ? )''', (name1, ))
		conn.commit()
		text.write("\n\n")
		i=i+1
	j=j+1
#for item in nameList:
#	print item
#	text.write(item)
text.close()