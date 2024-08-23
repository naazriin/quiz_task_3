import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:my-secret-pw@localhost:3307/task3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app) 
migrate = Migrate(app, db)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), nullable=False)
    released = db.Column(db.String(40), nullable=False)
    director = db.Column(db.String(40), nullable=False)
    genre = db.Column(db.String(40), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self,title, released, director, genre):
        self.title = title
        self.released = released
        self.director = director
        self.genre = genre

    def save(self):
        db.session.add(self)
        db.session.commit()


@app.route('/movie')
def moviee():
    all_movies = Movie.query.all()
    return render_template('index.html', all_movies=all_movies)
    

@app.route('/movie/<int:movie_id>')
def moviee_id(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('movie.html', movie=movie)


if __name__ == '__main__':
    app.run()



                        # Databazaya 6 fərqli film məlumatları daxil edilməsi (flask shell)
# mov1 =Movie(title="Inception", released="2010", director="Christopher Nolan", genre="Sci-Fi"),
# >>> mov1.save()
# >>> mov2 =  Movie(title="The Matrix", released="1999", director="Lana Wachowski, Lilly Wachowski", genre="Sci-Fi")
# >>> mov2.save()
# >>> mov3 = Movie(title="The Dark Knight", released="2008", director="Christopher Nolan", genre="Action")
# >>> mov3.save()
# >>> mov4 = Movie(title="The Shawshank Redemption", released="1994", director="Frank Darabont", genre="Drama")
# >>> mov4.save()
# >>> mov5 = Movie(title="Pulp Fiction", released="1994", director="Quentin Tarantino", genre="Crime")
# >>> mov5.save()
# >>> mov6 = Movie(title="Interstellar", released="2014", director="Christopher Nolan", genre="Sci-Fi")
# >>> mov6.save()