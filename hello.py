# test flask with this

from flask import Flask
app = Flask("hello")

@app.route('/')
def hello():
    return 'hello :)'

if __name__ == '__main__':
    app.run(debug=True)