# Введение во Flask
# MVC -(Model View Controller)
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
            <img src="f{url_for('static', filename='images/python2.jpg')}" alf="Pethon">
        </body>
        </html>
    """



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    # Адрес локального хоста