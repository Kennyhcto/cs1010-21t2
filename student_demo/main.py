# Code used: 4-1 Web intro/2_2_passing_data.py

from flask import Flask, request
from pyhtml import html, title, body, label, p, table, tr, td, strong, head, form, input_

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
            (
                label("Name: "),
                input_(type="text", name="user_name"),
                input_(type="Submit", value="Say Goodbye")
            )
        )
    )
    return str(code)

@app.route('/goodbye', methods=["POST"])
def goodbye():

    #print(request.form)
    print(f"{request.form=}")
    name = request.form['user_name']

    code = html(
        head(
            title("First PyHTML Program")
        ),
        body(
            p(f"Goodbye {name}!!"),
        )
    )
    return str(code)



if __name__ == "__main__":
    app.run(debug=True)