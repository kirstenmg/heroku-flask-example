from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("base.html",
        page='home page',
        content='Hello world')
    
if __name__ == '__main__':
    #app = create_app()
    app.run()
