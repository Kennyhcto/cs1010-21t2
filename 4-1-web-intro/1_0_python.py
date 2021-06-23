from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    my_html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Welcome Page</title>
        </head>
        <body>
            <h1>Welcome to COMP1010</h1>
            <h3>Greeting</h3>
            <p>I hope you're enjoying this lecture.</p>
        </body>
    </html>"""
    return my_html

if __name__ == "__main__":
    app.run(debug=True)