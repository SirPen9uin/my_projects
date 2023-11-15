import psycopg2

def create_tables():
    with conn.cursor() as cur:
        cur.execute('''
                DROP TABLE Clients_numbers;
                DROP TABLE Clients;
                ''')
        cur.execute('''
                CREATE TABLE IF NOT EXISTS Clients(
                    PRIMARY KEY (client_id),
                    client_id SERIAL,
                    client_first_name VARCHAR(40),
                    client_last_name VARCHAR(40),
                    client_email VARCHAR(80)
                    );
                    ''')
        cur.execute('''
                CREATE TABLE IF NOT EXISTS Clients_numbers(
                    PRIMARY KEY (number_id),
                    number_id SERIAL,
                    client_id INT REFERENCES Clients(client_id),
                    phone VARCHAR(15)
                    );
                    ''')
        conn.commit()

def new_client(first_name: str, last_name: str, email: str, phone: str=None):
    with conn.cursor() as cur:
        cur.execute('''
                INSERT INTO clients(client_first_name, client_last_name, client_email)
                VALUES (%s, %s, %s);
                ''', (first_name, last_name, email))
        if phone:
            cur.execute('''
                    SELECT client_id
                      FROM clients;
                      ''', )
            id = cur.fetchone()
            cur.execute('''
                    INSERT INTO Clients_numbers(client_id, phone)
                    VALUES (%s, %s);
                    ''', (id, phone))
        conn.commit()
def add_phone(client_id: int, phone: str):
    with conn.cursor() as cur:
        cur.execute('''
                INSERT INTO Clients_numbers(client_id, phone)
                VALUES (%s, %s);
                ''', (client_id, phone))
        conn.commit()

def client_info_update(client_id: int, first_name: str=None, last_name: str=None, email: str=None):
    with conn.cursor() as cur:
        cur.execute('''
                SELECT client_first_name, client_last_name, client_email
                  FROM clients
                 WHERE client_id=%s;
                 ''', (client_id,))
        currient_info = cur.fetchone()
        if first_name is None:
            first_name = currient_info[0]
        if last_name is None:
            last_name = currient_info[1]
        if email is None:
            email = currient_info[2]
        cur.execute('''
                UPDATE Clients
                   SET client_first_name=%s, client_last_name=%s, client_email=%s
                 WHERE client_id=%s;
                ''', (first_name, last_name, email, client_id))
        conn.commit()

def del_phone(client_id: int, phone: str):
    with conn.cursor() as cur:
        cur.execute('''
                DELETE FROM Clients_numbers
                 WHERE client_id=%s AND phone=%s;
                ''', (client_id, phone))
        conn.commit()

def del_client(client_id: int):
    with conn.cursor() as cur:
        cur.execute('''
                DELETE FROM Clients_numbers
                      WHERE client_id=%s;
                DELETE FROM Clients
                      WHERE client_id=%s;
                ''', (client_id, client_id))
        conn.commit()

def find_client(first_name: str=None, last_name: str=None, email: str=None, phone: str=None):
    if not any([first_name, last_name, email, phone]):
        raise ValueError("Хотя бы один из параметров должен быть указан")
    else:
        with conn.cursor() as cur:
            if phone:
                cur.execute('''
                SELECT client_id, client_first_name, client_last_name, client_email
                  FROM clients
                 WHERE client_id =
                       (SELECT client_id
                          FROM clients_numbers
                         WHERE phone=%s);
                         ''', (phone,))
            else:
                cur.execute('''
                    SELECT client_id, client_first_name, client_last_name, client_email
                      FROM Clients
                     WHERE (client_first_name = %s) OR
                           (client_last_name = %s) OR
                           (client_email = %s);
                ''', (first_name, last_name, email))
            results = cur.fetchall()
            return results

print('''
Это программа для хранения персональных данных.
В данной программе используется база данных под названием personal_info''')
db_user = str(input('Введите пользователя базы данных: '))
db_password = str(input('Введите пароль от базы данных: '))

conn = psycopg2.connect(database='personal_info', user=db_user, password=db_password)


if __name__ == '__main__':
    create_tables()
    print('База данных успешно создана')
    print('Сейчас база данных пустая, предлагаю добавить первого клиента')
    first_name = str(input('Введите имя клиента: '))
    last_name = str(input('Введите фамилию клиента: '))
    email = str(input('Введите email клиента: '))
    phone = str(input('Введите номер телефона клиента: '))
    new_client(first_name, last_name, email, phone)
    print('''
    Первый клиент добавлен!
    Вам доступны следующие функции программы: ''')
    print('''
    1 - Поиск клиента по имени/фамилии/email/номеру телефона;
    2 - Добавление нового клиента;
    3 - Добавление дополнительного телефонного номера для существующего клиента;
    4 - Обновление информации по клиенту;
    5 - Удалить телефонный номер клиента;
    6 - Удалить клиента из базы данных;
    q - Выход из программы''')
    search_info = (
    '''Для поиска клиента в базе данных
    необходимо указать один из критериев поиска:
    1 - имя
    2 - фамилия
    3 - email
    4 - номер телефона''')
    action = ''
    while True:
        action = str(input('Какое действие хотите выполнить? '))
        if action == '1':
            print(search_info)
            search_param = str(input('Выберите цифру с критерием: '))
            if search_param == '1':
                first_name = str(input('Введите имя клиента: '))
                print(find_client(first_name=first_name))
            elif search_param == '2':
                last_name = str(input('Введите фамилию клиента: '))
                print(find_client(last_name=last_name))
            elif search_param == '3':
                email = str(input('Введите email клиента: '))
                print(find_client(email=email))
            elif search_param == '4':
                phone = str(input('Введите телефон клиента: '))
                print(find_client(phone=phone))

        elif action == '2':
            first_name = str(input('Введите имя клиента: '))
            last_name = str(input('Введите фамилию клиента: '))
            email = str(input('Введите email клиента: '))
            phone = str(input('Введите номер телефона клиента: '))
            new_client(first_name, last_name, email, phone)

        elif action == '3':
            client_id = int(input('Введите id клиента: '))
            phone = str(input('Введите номер телефона клиента: '))
            add_phone(client_id=client_id, phone=phone)

        elif action == '4':
            first_name = None
            last_name = None
            email = None
            client_id = int(input('Введите id клиента: '))
            first_name = str(input('Введите имя клиента: '))
            if not first_name:
                first_name = None
            last_name = str(input('Введите фамилию клиента: '))
            if not last_name:
                last_name = None
            email = str(input('Введите email клиента: '))
            if not email:
                email = None
            client_info_update(client_id=client_id, first_name=first_name, last_name=last_name, email=email)

        elif action == '5':
            client_id = int(input('Введите id клиента: '))
            phone = str(input('Введите телефон клиента: '))
            del_phone(client_id=client_id, phone=phone)

        elif action == '6':
            client_id = int(input('Введите id клиента: '))
            del_client(client_id=client_id)

        elif action == 'q':
            print('Хорошего дня!')
            break
