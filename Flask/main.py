from flask import Flask, request, redirect, render_template
from datetime import datetime
import sqlite3
# from querys import AllPosts

app = Flask(__name__)


def submit():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        author = "Paulinus"
        dated = str(datetime.today().time().strftime('%H:%M:%S'))
        con = sqlite3.connect('posts.db')
        cursor = con.cursor()
        query = "INSERT INTO post(title, content, author, date) VALUES('" + title + "', '" + content + "', '" + author + "', '" + dated + "')"
        cursor.execute(query)
        con.commit()
        con.close()

@app.route("/", methods=['GET', 'POST'])
def posts():
    # global all_posts
    submit()
    con = sqlite3.connect('posts.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM post")
    all_posts = cursor.fetchall()
    return render_template('posts.html', posted=all_posts)

@app.route('/delete/<int:id>')
def delete(id):
    con = sqlite3.connect('posts.db')
    cursor = con.cursor()
    cursor.execute("DELETE FROM post WHERE id=='"+str(id)+"'")
    con.commit()
    return redirect('/')

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)