class space(object):

    def __init__(self, description, movement):
        self.description = description
        self.movement = movement

    def move(self, direction):
        print self.movement[direction]



def main  ():
    main_room = space("main room!", {"forward":"Hit a wall!"})
    action = raw_input("What do you want to do? ")



    if action == "forward":
        main_room.move(action)
    else:
        print "I don't understand {0}".format(action)

if __name__ == "__main__":
    main ()
