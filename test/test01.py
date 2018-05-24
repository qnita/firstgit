from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():

    return 'index'

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)