from flask import Flask, render_template, request


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

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')