



space_list = {}
current_room = None
class space(object):

    def __init__(self, description, movement):
        self.description = description
        self.movement = movement

    def move(self, direction):
        global current_room
        if direction in self.movement:
            current_room = space_list[self.movement[direction]]
        else:
            print "Can't go that way!"
        print(current_room.description)


space_list["main_room"] = space("entrance description",
                                {"forward": "admin_office",
                                 "left": "entrance_hallway_left",
                                 "right": "entrance_hallway_right"})
space_list["admin_office"] = space("admin_office description", {})
space_list["entrance_hallway_left"] = space("entrance hallway left description", {"back" : "main_room"})

current_room = space_list["main_room"]
def main  ():
    not_done = True
    while(not_done):
        action = raw_input("What do you want to do? ")
        if action == "forward" or action == "left" or action == "right" or action == "back":
            current_room.move(action)
        else:
            print "I don't understand {0}".format(action)

if __name__ == "__main__":
    main ()
