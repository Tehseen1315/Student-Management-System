from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask(__name__)

# CONNECTING TO MySql
db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Tehseen@07",
    database="StudentDB"
)

            
cursor = db.cursor()

# Displaying all students on home page
@app.route("/")
def index():
    cursor.execute("SELECT * FROM Students")
    Students = cursor.fetchall()
    return render_template("index.html", Students = Students)

# Add Student
@app.route("/add", methods =["POST"])
def add_student():
    name = request.form["name"]
    age = request.form["age"]
    grade = request.form["grade"]
    cursor.execute("INSERT INTO Students(name,age,grade) VALUES (%s,%s,%s)",(name,age,grade))
    db.commit()
    return redirect(url_for("index"))

# Delete Student 
@app.route("/delete/<int:id>")
def delete_student(id):
    cursor.execute("DELETE FROM Students WHERE id=%s" , (id,))
    db.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
