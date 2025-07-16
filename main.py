 Введение во Flask
 MVC -(Model View Controller)
 from flask import Flask, url_for

 app = Flask(__name__)
 debug = False


 @app.route('/')
 @app.route('/index')
 def index():
     print('Вызвана функция index')
     return 'Привет, Flask'


 @app.route('/about')
 def about():
     print('вызвана функция about')
     return 'О нас'

 @app.route('/countdown')
 def cd():
     lst = [str(x) for x in reversed(range(10))]
     lst.append('Полетели!!!')
     return '<5>'.join(lst)


 @app.route('/image')
 def show_image():
     return f'<img src="{url_for('static', filename='images/python.jpg')}">'


 @app.route('/sample-page')
 def sample_page():
     return f""" <!DOCTYPE html>
         <html lang="ru">
         <head>
             <meta charset="UTF-8">
             <title>Title</title>
         </head>
         <body>
             <img src="url_for('static', filename='images/python2.jpg'" alt="Pethon">
         </body>
         </html>
     """


 @app.route('/sample-page2')
 def sample_page2():
     with open('temp.html', 'r') as html:
         return html.read()


 if __name__ == '__main__':
     app.run(host='localhost', port=5000, debug=debug)
     # Адрес локального хоста


<string> - #по умолчанию строка
 <int:number> - #целое
 <float:number> - #дес.дробь
<path:p> - #может содержать слэши для указания пути
 <uuid:id> - #строка-идентификатор (16 - байт в HEX-формате)
 app.route('/greeting/<user>/<int:id_num>')
 def greeting(user):
     return f'Привет, {user} c id={id_num}

 @app.route('/get-user')
 @app.route('/get-user/<int:id_num>')
 def get_user(id_num):
     if id_num is None:
         return 'Нет номера записи'
     con = sqlite3.connect('db/movies.sqlite')
     cur = con.cursor()
     query = f'SELECT name FROM users trip_id{id_num}'
     response = cur.execute(query)
     result = response.fetchone()
     #print(result)
     cur.close()
     con.close()
     return str(result[0])
     def get_user(id_num):
     return f'''<table border="1">
    <tr>
    <td>ФИО</td>
    <td>Город</td >
    </tr>
    <tr>
    <td>{name}</td>
    <td>{name}</td>
    </tr>
    </table>'''