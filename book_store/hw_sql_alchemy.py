import sqlalchemy
from sqlalchemy.orm import sessionmaker
from book_store.hw_models import engine, create_tables, engine, Publisher, session, Author, Book, Shop, Stock, Sale, search_by_author, search_by_author_id


create_tables(engine)

publisher1 = Publisher(name='Эксмо')
publisher2 = Publisher(name='Издательство АСТ')
session.add_all([publisher1, publisher2])
session.commit()

author1 = Author(name='Виктор Пелевин')
author2 = Author(name='Стивен Кинг')
author3 = Author(name='Джоан Роулинг')
author4 = Author(name='Анджей Сапковский')
session.add_all([author1, author2, author3, author4])
session.commit()

book1 = Book(title='KGBT+', publisher=publisher1, author=author1)
book2 = Book(title='Сияние', publisher=publisher2, author=author2)
book3 = Book(title='Ведьмак. Последнее желание', publisher=publisher2, author=author4)
book4 = Book(title='Меч предназначения', publisher=publisher2, author=author4)
book5 = Book(title='Кровь эльфов', publisher=publisher2, author=author4)
book6 = Book(title='Кэрри', publisher=publisher2, author=author2)
book7 = Book(title='Гарри Поттер и филосовский камень', publisher=publisher1, author=author3)
book8 = Book(title='Гарри Поттер и тайная комната', publisher=publisher1, author=author3)
book9 = Book(title='Гарри Поттер и узник Азкабана', publisher=publisher1, author=author3)
book10 = Book(title='Гарри Поттер и Кубок Огня', publisher=publisher1, author=author3)
book11 = Book(title='Гарри Поттер и Орден Феникса', publisher=publisher1, author=author3)
book12 = Book(title='Гарри Поттер и Принц Полукровка', publisher=publisher1, author=author3)
book13 = Book(title='Гарри Поттер и Дары смерти', publisher=publisher1, author=author3)
session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13])
session.commit()

shop1 = Shop(name='Литрес')
shop2 = Shop(name='Ozon')
shop3 = Shop(name='Читай город')
shop4 = Shop(name='Буквоед')
session.add_all([shop1, shop2, shop3, shop4])
session.commit()

stock1 = Stock(book=book1, shop=shop1, count=1000)
stock2 = Stock(book=book1, shop=shop2, count=200)
stock3 = Stock(book=book1, shop=shop3, count=130)
stock4 = Stock(book=book2, shop=shop4, count=60)
stock5 = Stock(book=book3, shop=shop3, count=70)
stock6 = Stock(book=book4, shop=shop3, count=80)
stock7 = Stock(book=book5, shop=shop3, count=75)
stock8 = Stock(book=book6, shop=shop2, count=48)
stock9 = Stock(book=book7, shop=shop2, count=32)
stock10 = Stock(book=book8, shop=shop2, count=36)
stock11 = Stock(book=book9, shop=shop2, count=42)
stock12 = Stock(book=book10, shop=shop2, count=0)
stock13 = Stock(book=book11, shop=shop2, count=21)
stock14 = Stock(book=book12, shop=shop2, count=9)
stock15 = Stock(book=book13, shop=shop2, count=18)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12, stock13, stock14, stock15])
session.commit()

sale1 = Sale(price=450.36, date_sale='2023-02-18', stock=stock1, count=20)
sale2 = Sale(price=490.10, date_sale='2023-02-26', stock=stock2, count=13)
sale3 = Sale(price=530.57, date_sale='2023-02-13', stock=stock3, count=8)
sale4 = Sale(price=640.25, date_sale='2023-02-06', stock=stock4, count=3)
sale5 = Sale(price=867.54, date_sale='2023-02-28', stock=stock5, count=2)
sale6 = Sale(price=523.67, date_sale='2023-02-25', stock=stock6, count=6)
sale7 = Sale(price=120.90, date_sale='2023-02-19', stock=stock7, count=9)
sale8 = Sale(price=358.00, date_sale='2023-02-14', stock=stock8, count=7)
sale9 = Sale(price=265.55, date_sale='2023-02-25', stock=stock9, count=2)
sale10 = Sale(price=643.20, date_sale='2023-02-02', stock=stock10, count=13)
sale11 = Sale(price=380.75, date_sale='2023-02-03', stock=stock11, count=15)
sale12 = Sale(price=430.40, date_sale='2023-02-01', stock=stock12, count=9)
sale13 = Sale(price=480.25, date_sale='2023-02-08', stock=stock13, count=5)
sale14 = Sale(price=580.95, date_sale='2023-02-09', stock=stock14, count=7)
sale15 = Sale(price=1120.45, date_sale='2023-02-23', stock=stock15, count=0)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12, sale13, sale14, sale15])
session.commit()

session.close()

if __name__ == '__main__':
    name = input("Введите имя автора или его id: ")
    if name.isalpha():
        search_by_author(name)
    elif name.isdigit():
        search_by_author_id(name)