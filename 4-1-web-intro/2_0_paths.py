from flask import Flask
from pyhtml import html, title, body, p, table, tr, td, strong, head

app = Flask(__name__)

@app.route('/')
def hello():
    code = html(
        head(
            title("First PyHTML Program")
        ),
        body(
            p("Hello everyone!!"),
        )
    )
    return str(code)

@app.route('/goodbye')
def goodbye():
    code = html(
        head(
            title("First PyHTML Program")
        ),
        body(
            p("Goodbye!!"),
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)