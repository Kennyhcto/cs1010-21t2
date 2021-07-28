class Person:
    def __init__(self, zid, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.zid = zid

    def print_name(self):
        print(self.fname + " " + self.lname)

    # Given 2 objects of type Person, checks if their zids are equal
    # This method is called when == is used
    def __eq__(self, other):
        return isinstance(other, Person) and self.zid == other.zid
        # return type(other)==type(self) and self.zid == other.zid


def main():
    # Create a person object and print name
    sim = Person("3207186", "Sim", "Mautner")
    sim.print_name()
    liz = Person("1234567", "Liz", "Willer")
    liz.print_name()
    print(sim.fname)
    print(sim.lname)

    # Equals?
    print(f"Is sim equal to liz? {sim == liz}")
    sim2 = Person("3207186", "Sim", "Mautner")

    print(f"Is sim equal to sim2? {sim == sim2}")



if __name__== "__main__":
    main()