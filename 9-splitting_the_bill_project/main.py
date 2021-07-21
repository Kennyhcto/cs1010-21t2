from flask import Flask, request, session
from pyhtml import html, title, select, option, label, br, body, p, table, tr, td, strong, head, h1, form, input_, h3

import json

#import stb_database.py

app = Flask(__name__)
app.config['SECRET_KEY'] = '8pXH18iVHM_pySw6PKrFK4NFD8yr9oo-Z7VxFnVsVvQ'

# creating a drop-down list with options
def get_select_list(items):
    select_list = []
    for item in items:
        select_list.append(
            option(value=item)(item)
        )
    return select_list


# get the radio buttons for selecting Group, Person or Menu Item
def get_radio_buttons(group_name, labels, selected):
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

def read_json_file():
  f = open('9-splitting_the_bill_project/files/saved_data.json', 'r')
  all_data = json.loads(f.read())
  f.close()
  return all_data['groups'],all_data['people'],all_data['menu_items']

def write_json_file(groups, people, menu_items):
    all_data = {}
    all_data['groups'] = groups
    all_data['people'] = people
    all_data['menu_items'] = menu_items

    f = open('9-splitting_the_bill_project/files/saved_data.json', 'w')
    f.write(json.dumps(all_data))
    f.close()

@app.route('/', methods=['GET','POST'])
def main():

    groups = session.get('groups', {})
    people = session.get('people', {})
    menu_items = session.get('menu_items', [])

    adding_input_fields = []
    labels = ["Group", "Person", "Menu Item"]

    # if the user submitted a form
    if request.method == 'POST':
        if 'save' in request.form:
            write_json_file(groups, people, menu_items)
            adding_input_fields = get_radio_buttons("add_type", labels, "")

        if 'load' in request.form:
            groups,people,menu_items = read_json_file()
            adding_input_fields = get_radio_buttons("add_type", labels, "")

        if 'clear_data' in request.form:
            session.clear()
            groups = session.get('groups', {})
            people = session.get('people', {})
            menu_items = session.get('menu_items', [])
            adding_input_fields = get_radio_buttons("add_type", labels, "")

        if 'submit_group' in request.form:
            group_name = request.form['name']
            groups[group_name] = {'size':0, 'total_spent':0}
        elif 'submit_person' in request.form:
            person_name = request.form['name']
            group_name = request.form['group_name']
            people[person_name] = {'group':group_name, 'amount_paid':0}
        elif 'submit_item' in request.form:
            item_name = request.form['name']
            item_group = request.form['group_name']
            item_price = request.form['price']
            item_qty = request.form['qty']
            menu_items.append({'name':item_name,
                               'group':item_group,
                               'price':item_price,
                               'qty':item_qty})

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
                    input_(type="submit", name="submit_group")
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
                    input_(type="submit", name="submit_person")
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

    for group in groups:
        left_panel.append(h3(group))
        left_panel.append(br)
        for person, p_data in people.items():
            # for person in people:
            #   p_data = people[person]
            if p_data['group'] == group:
                left_panel.append(person)
                left_panel.append(br)
        for item in menu_items:
            if item['group'] == group:
                left_panel.append(f"{item['name']}: ${float(item['price']):.2f} x {item['qty']}")
                left_panel.append(br)



    left_panel.append(form(action="/")(
        input_(type="submit", value="Save", name="save"),br,
        input_(type="submit", value="Load", name="load"),br,
        input_(type="submit", value="Clear Data", name="clear_data")
    ))



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

    # Save our data as cookies
    session['groups'] = groups
    session['people'] = people
    session['menu_items'] = menu_items
    session.modified = True

    return str(code)

if __name__ == "__main__":
    app.run(debug=True)