from flask import Flask, request, session
from pyhtml import html, form, label, head, body, input_, h3, ul, li
#from pyhtml import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Og5WDE6A8OidZG-fqsLgo2afWS18VIhmOVdMaYOCr3E'

@app.route('/', methods=['POST', 'GET'])
def main():

    # Make sure items is in the session,
    # even if it's just an empty list
    if 'items' not in session:
        session['items'] = []

    # Get the most recent item from the form
    if request.method == 'POST':
        if 'clear_list' in request.form.keys():
            session.clear()
            session['items'] = []
        elif 'add_item' in request.form.keys():
            item = request.form['item']
            print(f"{item=}")
            session['items'].append(item)
            session.modified = True

    # Create pyhtml bullet list of items
    display_list_of_items = []
    for item in session['items']:
        display_list_of_items.append(li(item))

    # Create the html with a list and form
    content = html(
        body(
            form(action="/")(
                input_(type="text", name="item"),
                input_(type="submit", name='add_item')
            ),
            h3('List'),
            ul(display_list_of_items),
            form(action="/")(
                input_(type="submit", value="Clear", name="clear_list")
            )
        )
    )

    return str(content)



if __name__ == "__main__":
    app.run(debug=True)