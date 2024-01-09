from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM todos")
    todos = cur.fetchall()
    cur.close()
    return render_template('index.html', todos=todos)
    #return jsonify(todos)

@app.route('/create_todo', methods=['GET', 'POST'])
def create_todo():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO todos (name, status) VALUES (%s, %s)", (name, status))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
    else:
        return render_template('create.html')

@app.route('/update_todo/<int:id>', methods=['GET', 'PUT'])
def update_todo(id):
    cur = mysql.connection.cursor()

    if request.method == 'PUT':
        new_name = request.form['name']
        new_status = request.form['status']

        cur.execute("UPDATE todos SET name = %s, status = %s WHERE id = %s", (new_name, new_status, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
    else:
        cur.execute("SELECT * FROM todos WHERE id = %s", (id,))
        todo = cur.fetchone()
        cur.close()
        return render_template('update.html', todo=todo)


@app.route('/delete_todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))