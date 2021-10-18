import sqlite3
db = sqlite3.connect("user.db")
view = db.cursor()
view.execute("SELECT * FROM user")
content = view.fetchall()
print(content)
db.close()
