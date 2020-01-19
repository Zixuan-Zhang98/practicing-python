from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Zixuan'
    letters = list(name)
    pup_dict = {'pup_name' : 'Sammy'}
    # flask automatically look in to the same level directory called 'templates'
    return render_template('basic.html', name=name, letters=letters, pup_dict=pup_dict)

if __name__ == '__main__':
    app.run(debug=True)