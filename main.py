from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("base.html",
        title='Hello World!',
        header='This is a header',
        content='<p>This is where content can go.</>')
    
if __name__ == '__main__':
    #app = create_app()
    app.run()
