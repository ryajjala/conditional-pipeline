import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.template_folder = os.path.abspath('templates')  # Set the template folder to the 'templates' directory

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        if operator == 'add':
            result = num1 + num2
            operation = '+'
        elif operator == 'subtract':
            result = num1 - num2
            operation = '-'
        elif operator == 'multiply':
            result = num1 * num2
            operation = '*'
        elif operator == 'divide':
            result = num1 / num2
            operation = '/'

        return render_template('calculator.html', num1=num1, num2=num2, operation=operation, result=result)

    return render_template('calculator.html')

if __name__ == '__main__':
    from gunicorn.app.base import BaseApplication

    class FlaskApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '127.0.0.1:7070',  # Set the host and port to bind
        'workers': 4,              # Set the number of worker processes
        'daemon': True             # Run the application in the background
    }

    FlaskApplication(app, options).run()