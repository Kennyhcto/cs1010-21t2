from flask import Flask
from pyhtml import html, title, body, p, table, tr, td, strong, head, form, input_

app = Flask(__name__)

@app.route('/')
def hello():
    code = html(
        head(
            title("First PyHTML Program")
        ),
        body(
            p("Hello everyone!!"),
            form(action="goodbye")
            (input_(type="Submit", value="Say Goodbye"))
        )
    )
    return str(code)

@app.route('/goodbye', methods=["POST"])
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