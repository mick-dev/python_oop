# how to record data
# tuple
def demo_tuple():
    p12 = "Joe", "Gomez", 12
    print(p12)
    print(p12[1])

# dictionary >> keep pair data (key and value)
def demo_dict():
    p12 = {"fname": "Joe", "lname": "Gomez", "number": 12}
    print(p12)
    print(p12["lname"])

# use class
class Player: # this class like the variable
    pass

def demo_simple_plyaer_class():
    p12 = Player() # p12 -> instanct
    p12.fname = "Joe" # fname is atribute/property
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname)

# use the class
class Player2:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.number = 0

# how to use the Player2
def demo_simple_player_class2():
    p12 = Player2()
    p12.fname = "Joe"
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname)

# can pass the value inside class
class Player3:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

def demo_simple_player_class3():
    p12 = Player3("Joe", "Gomez", 12)
    print(p12.lname)

if __name__ == '__main__':
    # demo_tuple()
    # demo_dict()
    # demo_simple_plyaer_class()
    # demo_simple_player_class2()
    demo_simple_player_class3()