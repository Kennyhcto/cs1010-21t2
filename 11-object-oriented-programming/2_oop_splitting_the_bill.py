class Person:
    def __init__(self, name):
        self.name = name
        self.paid = 0

class MenuItem:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Group:
    def __init__(self, name):
        self.name = name
        self.people = []
        self.items = []

    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.items.append(item)

    def add_person(self, person):
        if isinstance(person, Person):
            self.people.append(person)
    
    def display_summary(self):
        total_amount = 0
        for item in self.items:
            total_amount += item.price * item.qty
        
        amount = 0
        if len(self.people):
            amount = total_amount/len(self.people)
        print(f"Each person owes {amount:.2f}.")
        for person in self.people:
            print(person.name)
        for item in self.items:
            print(f"{item.name}: {item.qty}x${item.price:.2f}={item.qty*item.price:.2f}")

def main():
    groups = [Group('A'), Group('B'), Group('C')]
    groups[0].add_person(Person('Sim'))
    groups[0].add_person(Person('Sienna'))
    groups[0].add_person(Person('Emily'))
    groups[0].add_item(MenuItem('Pizza', 20, 2))
    groups[0].add_item(MenuItem('Ice Cream', 4, 3))
    for group in groups:
        group.display_summary()

    # Other classes/objects we've seen before:
    my_string = "hello"
    # Function
    print(len(my_string))
    # Method in string class
    print(my_string.count('e'))
    

if __name__=="__main__":
    main()