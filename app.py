# Flask Web Framework

from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def celsius_to_fahrenheit_page(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{fahrenheit}"


if __name__ == '__main__':
    app.run()
