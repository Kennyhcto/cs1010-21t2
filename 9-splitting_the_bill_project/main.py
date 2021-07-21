from flask import Flask, request, session
from pyhtml import html, title, select, option, label, br, body, p, table, tr, td, strong, head, h1, form, input_, h3

#import stb_database.py

app = Flask(__name__)

# creating a drop-down list with options
def get_select_list(items):
    select_list = []
    for item in items:
        select_list.append(
            option(value=item)(item)
        )


# get the radio buttons for selecting Group, Person or Menu Item
def get_radio_buttons(group_name, labels, selected):
    print(f"Getting radio buttons {selected=} {labels=}")
    buttons = []
    for text in labels:
        if text == selected:
            buttons.append(input_(
                type="radio", # radio button
                name=group_name, # part of the add_type group (only one radio button per group is selected at a time)
                value=text, # allows us to get which one was selected
                id=text, # allows us to click the label rather than the button
                checked="checked"))
        else:
            buttons.append(input_(
                type="radio", # radio button
                name=group_name, # part of the add_type group (only one radio button per group is selected at a time)
                value=text, # allows us to get which one was selected
                id=text)) # allows us to click the label rather than the button
        buttons.append(label(for_=text)(text))
        buttons.append(br)
    buttons.append(input_(type="submit"))
    buttons.append(br)
    buttons.append(br)
    return buttons


@app.route('/', methods=['GET','POST'])
def main():

    groups = {}
    people = {}
    menu_items = []

    adding_input_fields = []
    labels = ["Group", "Person", "Menu Item"]

    # if the user submitted a form
    if request.method == 'POST':
        # if it's the radio button of "what to add"
        if 'add_type' in request.form:
            # check which type they want to add
            if request.form['add_type'] == 'Group':
                # for a group, we just need the group name
                # (textbox with a label)
                adding_input_fields = [
                    get_radio_buttons("add_type", labels, "Group"),
                    label("Name: "),
                    input_(type="text", name="name"),br,
                    input_(type="submit", name="submit_item")
                ]
            elif request.form['add_type'] == 'Person':
                # for a person, we need their name and which group they're in
                # (textbox with a label and a dropdown menu to select the group)
                adding_input_fields = [
                    get_radio_buttons("add_type", labels, "Person"),
                    label("Name: "),
                    input_(type="text", name="name"),br,
                    label("Group: "),
                    select(name="group_name")(get_select_list(groups)),br,
                    input_(type="submit", name="submit_item")
                ]
            elif request.form['add_type'] == 'Menu Item':
                # for a menu item: name, group, price and qty
                adding_input_fields = [
                    get_radio_buttons("add_type", labels, "Menu Item"),
                    label("Name: "),
                    input_(type="text", name="name"),br,
                    label("Group: "),
                    select(name="group_name")(get_select_list(groups)),br,
                    label("Price: "),
                    input_(type="number", name="price"),br,
                    label("Qty: "),
                    input_(type="number", name="qty"),br,
                    input_(type="submit", name="submit_item")
                ]
    else:
        adding_input_fields = get_radio_buttons("add_type", labels, "")

    left_panel = []
    left_panel.append("left side")



    adding_form = form(action="/")(
        h3("Add"),
        # Radio buttons for what we are adding
        #get_radio_buttons(labels, "Group"),
        
        # Add specific fields based on what has already
        # been selected in the radio buttons
        adding_input_fields
    )


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