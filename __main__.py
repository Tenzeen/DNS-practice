from flask import Flask

app = Flask(__name__)

@app.route('/')
def default_home():
    return 'Hello! Welcome to ZinCare!'

@app.route('/careers')
def careers():
    return 'This is the career page...'

@app.route('/dashboards')
def dashboards():
    return 'This is our dashboards page...'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)