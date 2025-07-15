# Базы данных (запись)
# """
# # 1. Импорт библиотеки SQL
# # 2. Подключение к БД
# # 3. Назначить
# # 4. Работа с БД (Запросы и ответы)
# # 5. Отключаемся от БД
# """
# import sqlite3
#
# # Подключаемся
# connection = sqlite3.connect('db/movies.sqlite')
#
# # Курсор
# cursor = connection.cursor()
#
# # Запрос (с помощью курсора)
# result = cursor.execute(
#     """
#     SELECT title, year FROM films
#     WHERE year BETWEEN 2001 AND 2005
#     """
# )
#
# print result.fetchall()

# for title, year in array:
#     print(title, year)


import sqlite3

class Crud:
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)
        self._cur = self._conncursor()

    def create(self, table_name, name, age):
        self._cur.execute(
            f"""
            INSERT INTO users(name, age)
        VALUES(?,?)
        """, (name, int(age))
        )
        self._conn.commit()




    def delete(selfself, in_num, table_name):
            self._cur.execute(
                f'DELETE FROM {table_name} WHERE id={id_num}'
            )
            self._conn.commit()

    def read(self, table_name):
        res = self._cur.execute(
             f'SELECT * FROM {table_name}'
        ).fetchmall()
        for num, name, age in res:
             print(id, name, age)

    def update(self, table_name, id_num, name=None, age=None):

        query = f'UPDATE' {table_name} SET name={name}, age={age}, id={id_num}'
        self._cur.execute(
            query
        )
        self._conn.commit()



    def delete(selfself, in_num, table_name):
        self._cur.execute(
            f'DELETE FROM {table_name} WHERE id={id_num}'
        )
        self._conn.commit()

    # method override (переопределяем метод уничтожения объекта)
    def __del__(self):
        self._conn.close() # отключаем курсор
        self._conn.close() # отключаем от БД

db = Crud('db/movies.sqlite')
#db.delete(3, 'users')
db.update ('users', 'Евгений', 19)
db.read('users')

print()











