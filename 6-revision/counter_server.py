from flask import Flask, session
from pyhtml import html, title, body, p, table, tr, td, strong, head

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Og5WDE6A8OidZG-fqsLgo2afWs18VIhmOVdMaYOCr3E'

@app.route('/')
def main():

    if 'visits' not in session:
        session['visits'] = 0
    session['visits'] += 1
    

    code = html(
        body(
            p(f"Welcome to your {session['visits']} visit.")
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)