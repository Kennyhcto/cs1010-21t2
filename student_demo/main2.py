# Code used: 4-1 Web intro/2_2_passing_data.py

# This time, having the same page

from flask import Flask, request
from pyhtml import html, title, body, label, p, table, tr, td, strong, head, form, input_

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello():

    stuff_to_say = []
    stuff_to_say.append(p("I think you're awesome. Do I know who you are?"))

    if request.method == 'POST':
        # we recieved a form
        # get the name out of the form
        name = request.form['user_name']
        stuff_to_say.append("I do know!! You're "+name)
    else:
        stuff_to_say.append("No. I don't know.")

    code = html(
        head(
            title("First PyHTML Program")
        ),
        body(
            p("Hello everyone!!"),
            stuff_to_say,
            form(action="/")
            (
                label("Name: "),
                input_(type="text", name="user_name"),
                input_(type="Submit", value="Say Goodbye")
            )
        )
    )
    return str(code)

'''
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
'''

if __name__ == "__main__":
    app.run(debug=True)