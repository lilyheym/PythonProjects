import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
      cur = conn.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment (ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                              col_fileName TEXT)")
      conn.commit()

conn = sqlite3.connect('assignment.db')



#list of name
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                  'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# loop through each object in the tuple to find the file that ends in .txt

for x in fileList:
      if x.endswith('.txt'):
            with conn:
                  cur = conn.cursor()

                  cur.execute("INSERT INTO tbl_assignment (col_fileName) VALUES (?)", (x,))
                  print(x)

conn.close()
            
