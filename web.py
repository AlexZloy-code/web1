from flask import Flask, render_template, request, url_for

import os
import random
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        prof = 'IT'
    else:
        prof = 'NS'

    return render_template('Tasks/Task1.html', prof=prof)


@app.route('/list_prof/<type>')
def list_prof(type):
    mas = [
        'инженер-исследователь',
        'пилот',
        'строитель',
        'экзобиолог',
        'врач',
        'инженер по терраформированию',
        'климатолог',
        'специалист по радиационной защите',
        'астрогеолог',
        'гляциолог',
        'инженер жизнеобеспечения',
        'метеоролог',
        'оператор марсохода',
        'киберинженер',
        'штурман',
        'пилот дронов',
    ]
    return render_template('Tasks/Task2.html', type=type, mas=mas)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('Tasks/Task3.html', 
    title='Анкета',
    surname='Золотой',
    name='Саня',
    education='Высшее оконченое',
    profession='Прогер на Пиииитоне',
    sex='male',
    motivation='Хочу найти приключений на 5-ую точку',
    ready= True
)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login_form.html')
    elif request.method == 'POST':
        print(request.form['ID_astr'])
        print(request.form['password_astr'])
        print(request.form['ID_cop'])
        print(request.form['password_cop'])
        return "Форма отправлена"
    

@app.route('/distribution')
def distribution():
    return render_template('Tasks/Task4.html', list_of_kocmonaft=['Кто-то 1', 'Кто-то 1', 'Я хочу быть капитаном', 'Кто-то 20'])


@app.route('/table/<pol>/<int:age>')
def table(pol, age):
    if pol == 'male':
        r = g = random.randint(0, 50)
        color = color = f'#{hex(r)[2:]}{hex(g)[2:]}FF'
    elif pol == 'female':
        g = b = random.randint(0, 78)
        color = f'#FF{hex(g)[2:]}{hex(b)[2:]}'
    else:
        r = b = random.randint(0, 116)
        color = f'#{hex(r)[2:]}FF{hex(b)[2:]}'
    return render_template('Tasks/Task5.html', age=(age < 21), color=color)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    imgs = [url_for('static', filename = f'image/galery/{i}') for i in list(filter(lambda x: 'jpg' in x or 'png' in x, os.listdir('static/image/galery')))]
    if request.method == 'GET':
        return render_template('Tasks/Task6.html', imgs=imgs)
    elif request.method == 'POST':
        f = request.files['file']
        path = os.path.join('static/image/galery', f.filename)
        f.save(path)
        return app.redirect('/galery')


@app.route('/member')
def member():
    with open('templates/members.json', 'r', encoding='utf8') as f:
        members = json.load(f)['members']
    return render_template('Tasks/Task7.html', members=members)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')