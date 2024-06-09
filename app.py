from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from ProyectoIng.routes import *

if __name__ == '__main__':
    app.run(debug=True)
