from flask import Flask
app = Flask(name)
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s:' % name
@app.route('/')
def hello_world():
    return 'Hello World'
if name == 'main':
    app.run(host='0.0.0.0', port=5000, debug=True)

