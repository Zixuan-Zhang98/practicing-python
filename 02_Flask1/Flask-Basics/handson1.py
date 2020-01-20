from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Puppy site"


@app.route('/puppy/<name>')
def puppy(name):
    if name[-1] != 'y' and name[-1] != 'Y':
        name += 'y'
    else:
        name = name[:-1] + 'iful'
    return f'Name: {name}'


if __name__ == '__main__':
    app.run(debug=True)
