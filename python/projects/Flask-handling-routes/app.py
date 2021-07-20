from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'

@app.route('/about')
def about():
    return '<h2>This is my about page </h2>'

@app.route('/error')
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>'

@app.route('/admin')
def admin():
    return redirect(url_for('error'))

@app.route('/hello')
def hello():
    return '<h1>Hello, World! </h1>'

@app.route('/greet_admin')
def greet_admin():
    return redirect(url_for(('greet'), name='Master Admin!!!!'))


if __name__=="__main__":
	app.run(debug=True)
	#app.run(host='0.0.0.0', port=80)
