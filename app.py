from flask import Flask, render_template, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.SNo}-{self.title}"
    

@app.route("/", methods=['GET','POST'])
def hello_world():

    if request.method == 'POST':
        title = request.form["title"]
        description = request.form["desc"]


        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html",allTodo=allTodo)

@app.route("/update/<int:SNo>", methods=['GET','POST'])
def update(SNo):
    todo = Todo.query.filter_by(SNo=SNo).first()
    if todo is None:
        abort(404)
    if request.method == 'POST':
        todo.title = request.form["title"]
        todo.description = request.form["desc"]
        db.session.commit()
        return redirect("/")
    return render_template("update.html",todo=todo)

@app.route("/delete/<int:SNo>")
def delete(SNo):
    todo = Todo.query.filter_by(SNo=SNo).first()
    if todo is None:
        abort(404)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
           
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates the .db file
        print("Database created successfully!")
    app.run(debug=True)