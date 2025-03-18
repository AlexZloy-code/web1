from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/training/<prof>')
def training(prof):
    print(prof, 'инженер' in prof.lower())
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        prof = 'IT'
    else:
        prof = 'NS'

    return render_template('Tasks/Task1.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')