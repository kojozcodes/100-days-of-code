# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute(
# #     "CREATE TABLE books ("
# #     "id INTEGER PRIMARY KEY, "
# #     "title varchar(250) NOT NULL UNIQUE, "
# #     "author varchar(250) NOT NULL, "
# #     "rating FLOAT NOT NULL"
# #     ")"
# # )
#
# cursor.execute(
#     "INSERT INTO books VALUES("
#     "1, 'Harry Potter', "
#     "'J. K. Rowling', "
#     "'9.3'"
#     ")"
# )
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=9.0)
    db.session.add(new_book)
    db.session.commit()
