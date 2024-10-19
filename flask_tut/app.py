from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# tasks = []

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', todos=tasks)

@app.route('/todo', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    new_task = Task(task=todo)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.filter_by(id=id).first()
    if request.method == 'POST':
        task.task = request.form['todo']
        db.session.commit()
        return redirect('/')
    return render_template("edit_task.html", task=task)

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

app.run(debug=True)