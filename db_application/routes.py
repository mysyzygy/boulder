from flask import render_template, request
from models import Person


def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template("index.html", people=people)
        elif request.method == 'POST':
            name = request.form['name']
            age = int(request.form['age'])
            job = request.form['job']

            person = Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()
            people = Person.query.all()
            return render_template("index.html", people=people)

    @app.route('/delete/<pid>', methods=["DELETE"])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        people = Person.query.all()
        return render_template("index.html", people=people)

    @app.route('/detail/<pid>')
    def detail(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template('detail.html', person=person)