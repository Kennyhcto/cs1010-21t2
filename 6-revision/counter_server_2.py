from flask import Flask, session, request
from pyhtml import html, title, body, p, table, tr, td, strong, head, form, input_

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Og5WDE6A8OidZG-fqsLgo2afWs18VIhmOVdMaYOCr3E'

@app.route('/', methods=["GET", "POST"])
def main():

    if 'visits' not in session:
        session['visits'] = 0
    
    if request.method == "POST":
        if "reset" in request.form:
            session['visits'] = 0


    session['visits'] += 1
    

    code = html(
        body(
            p(f"Welcome to your {session['visits']} visit."),
            form(action="/")(
                # Put our "Reset to Zero" button on our form
                input_(type="submit", value="Reset to Zero", name="reset")
            )
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)