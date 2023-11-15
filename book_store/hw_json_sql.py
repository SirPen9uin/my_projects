from hw_models import create_tables, engine, data_json


if __name__ == '__main__':

    create_tables(engine)

    data_json()