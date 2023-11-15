import json
import os
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from dotenv import load_dotenv
import psycopg2

load_dotenv()
DSN = os.getenv('MY_DSN')
engine = sqlalchemy.create_engine(DSN)



Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60))


class Author(Base):
    __tablename__ = 'author'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50))

    def __str__(self):
        return f'Author: {self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=80))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    id_author = sq.Column(sq.Integer, sq.ForeignKey('author.id'))
    publisher = relationship(Publisher, backref='book')
    author = relationship(Author, backref='book')

    def __str__(self):
        return f'{self.title}'


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60))

    def __str__(self):
        return f'{self.name}'

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer)
    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')

    def __str__(self):
        return f'{self.book}'



class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.DATE, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)
    stock = relationship(Stock, backref='sale')

    def __str__(self):
        return f'{self.stock}|{self.stock.shop}|{self.price}|{self.date_sale}'



def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def search_by_author(name: str):
    subq_author = session.query(Author).filter(Author.name.like(f'%{name}%')).subquery()
    subq_book = session.query(Book).join(subq_author, Book.id_author == subq_author.c.id).subquery()
    subq_stock = session.query(Stock).join(subq_book, Stock.id_book == subq_book.c.id).subquery()
    for c in session.query(Sale).join(subq_stock, Sale.id_stock == subq_stock.c.id).order_by(Sale.date_sale).all():
        print(c)
    session.close()

def search_by_author_id(name: int):
    subq_author = session.query(Author).filter(Author.id == name).subquery()
    subq_book = session.query(Book).join(subq_author, Book.id_author == subq_author.c.id).subquery()
    subq_stock = session.query(Stock).join(subq_book, Stock.id_book == subq_book.c.id).subquery()
    for c in session.query(Sale).join(subq_stock, Sale.id_stock == subq_stock.c.id).order_by(Sale.date_sale).all():
        print(c)
    session.close()

def data_json():
    with open('fixtures/books.json', 'r') as fb:
        data_json = json.load(fb)

    for data in data_json:
        model = {
            'publisher': Publisher,
            'author': Author,
            'book': Book,
            'shop': Shop,
            'stock': Stock,
            'sale': Sale
        }[data.get('model')]
        session.add((model)(id=data.get('pk'), **data.get('fields')))
    session.commit()

