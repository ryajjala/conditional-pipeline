import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.template_folder = os.path.abspath('templates')  # Set the template folder to the 'templates' directory

# Rest of your code...
from flask import Flask, request, render_template

app = Flask(__name__)

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
    app.run(port=7070)

