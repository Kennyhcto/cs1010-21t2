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
            table(
                tr(
                    td(strong("Movies")),
                    td(strong("Genres"))
                ),
                tr(
                    td("Toy Story"),
                    td("Family")
                )
            )
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)