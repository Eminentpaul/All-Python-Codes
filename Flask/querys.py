import sqlite3
con = sqlite3.connect('posts.db')
cursor = con.cursor()

table = """CREATE TABLE IF NOT EXISTS post(
    id integer primary key autoincrement,
    title text not null,
    content text not null,
    author text not null,
    date int not null
)"""

cursor.execute(table)
class AllPosts():
    def submit(self,title, content, author, date):
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        query = "INSERT INTO post VALUES('"+self.title+"', '"+self.content+"', '"+self.author+"', '"+self.date+"')"
        cursor.execute(query)
        con.commit()
        # con.close()

    def get_values(self):
        value = "SELECT * FROM post"
        cursor.execute(value)
        all_posts = cursor.fetchall()
        return all_posts
        con.close()


posts = AllPosts()
print(posts.get_values())