from flask import Flask, request, session
from pyhtml import html, title, select, option, label, body, p, table, tr, td, strong, head, h1, form, input_, h3

#import stb_database.py

app = Flask(__name__)

# creating a drop-down list with options
def get_select_list(items):
    select_list = []
    for item in items:
        select_list.append(
            option(value=item)(item)
        )

@app.route('/', methods=['GET','POST'])
def main():

    groups = {}
    people = {}
    menu_items = []

    adding_input_fields = []

    # if the user submitted a form
    if request.method == 'POST':
        # if it's the radio button of "what to add"
        if 'add_type' in request.form:
            # check which type they want to add
            if request.form['add_type'] == 'group':
                # for a group, we just need the group name
                # (textbox with a label)
                adding_input_fields = [
                    label("Name: "),
                    input_(type="text", name="name")
                ]
            elif request.form['add_type'] == 'person':
                # for a person, we need their name and which group they're in
                # (textbox with a label and a dropdown menu to select the group)
                adding_input_fields = [
                    label("Name: "),
                    input_(type="text", name="name"),
                    label("Group: "),
                    select(name="group_name")(get_select_list(groups))
                ]
            elif request.form['add_type'] == 'item':
                pass

    left_panel = []
    left_panel.append("left side")

    adding_form = form(action="/")(
        h3("Add"),
        # Radio buttons for what we are adding
        input_(type="radio", name="add_type", value="group"),
        label(for_="group")("Group"),
        input_(type="radio", name="add_type", value="person"),
        label(for_="person")("Person"),
        input_(type="radio", name="add_type", value="item"),
        label(for_="item")("Menu Item"),
        input_(type="submit"),
        # Add specific fields based on what has already
        # been selected in the radio buttons
        adding_input_fields
    )

# TODO make type selection stay selected
# TODO make page add fields when radio button is selected (nice to have feature)

    code = html(
        head(
            title("Splitting the Bill")
        ),
        body(
            h1("Splitting the Bill"),
            table(tr(td(left_panel),td(adding_form)))
        )
    )
    return str(code)

if __name__ == "__main__":
    app.run(debug=True)