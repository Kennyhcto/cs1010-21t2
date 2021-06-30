from flask import Flask, request
from pyhtml import html, form, label, head, body, input_, title, p, script

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    content = html(
        head(script(src='static/illegal_drugs.js')),
        body(
            form(action='thanks', name='drugs_form', onsubmit='adjust_answer();')(
                input_(type="radio", name="drugs", value="yes"),
                label(for_="yes")("Yes, I do illegal drugs"),
                input_(type="radio", name="drugs", value="no"),
                label(for_="no")("No, I don't illegal drugs"),
                input_(type="submit")
            )
        )
    )

    return str(content)

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    message = "Thank you for submitting " + request.form['drugs']
    return message

if __name__ == "__main__":
    app.run(debug=True)