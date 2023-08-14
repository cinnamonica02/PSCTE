from flask import request, Flask, render_template, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/')
def hello_world():
    return '<h1>Hello, World</h1>'

@app.route('/math', methods=['POST'])
def math_ops():
    # by using 'post' it means we are sending a form
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        #add
        if ops == 'add':
            #r = num1+num2
            #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
             result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 + num2)
        
        #substract
        if ops == 'subtract':
        #r = num1+num2
        #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
            result = 'The substraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 - num2)
        #multiply
        if ops == 'multiply':
        #r = num1+num2
        #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 * num2)
        #divide
        if ops == 'divide':
        #r = num1+num2
        #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
            result = 'The quotient of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 / num2)

        return render_template('results.html', result = result)


# app w post



@app.route('/postman_action', methods=['POST'])
def math_ops1():
    # by using 'post' it means we are sending a form
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        #add
        if ops == 'add':
            #r = num1+num2
            #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
             result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 + num2)
        
        #substract
        if ops == 'subtract':
        #r = num1+num2
        #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
            result = 'The substraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 - num2)
        #multiply
        if ops == 'multiply':
        #r = num1+num2
        #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 * num2)
        #divide
        if ops == 'divide':
        #r = num1+num2
        #result = 'The sum of '+ str(num1) + 'and ' + str(num2)
            result = 'The quotient of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 / num2)

        return jsonify(result)
    
app.debug = True
if __name__=='__main__':
    app.run(host='0.0.0.0')

