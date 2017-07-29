



space_list = {}
current_room = None
inventory = []
class space(object):

    def __init__(self, description, movement, items=None):
        self.description = description
        self.movement = movement
        self.items = items

    def move(self, direction):
        global current_room
        if direction in self.movement:
            current_room = space_list[self.movement[direction]]
        else:
            print "Can't go that way!"
        print(current_room.description)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

def pickup_dollar():
    global inventory
    if "dollar" not in inventory and "dollar" in current_room.get_items():
        current_room.remove_item("dollar")
        inventory.append("dollar")
def put_dollar_token_machine():
    global inventory
    if "dollar" in inventory and "token_machine" in current_room.get_items():
        inventory.remove("dollar")
        inventory.append("token")
def play_video_game():
    global inventory
    if "token" in inventory and "video_game" in current_room.get_items():
        inventory.remove ("token")
        inventory.append("clue")
def enter_combination(val1, val2, val3, val4):
    global inventory
    if "cabinet_with_lock" in current_room.get_items():
        print "cabinet, key entered: {0} {1} {2} {3}".format(val1, val2, val3, val4)
        if val1 == "2" and val2 == "0" and val3 == "0" and val4 == "4":
            inventory.append("logbook")
def read_clue():
    global inventory
    if "clue" in inventory:
        print "2 0 0 4"

def read_logbook():
    global inventory
    if "logbook" in inventory:
        print "you skim quickly to the end. on the last page, the book says the scientists in the research lab had accidentally opened a portal of sorts to a strange new world. almost immediately after beasts, aliens, came out, and started taking people back. whoever wrote this last entry was one of the last ones to be abducted. "

def go_to_room(room):
    global space_list
    global current_room
    current_room = space_list[room]

space_list["main_room"] = space("the main room, a room with a a hallway going left and right going deeper into the base.",
                                {"forward": "admin_office",
                                 "left": "entrance_hallway_left",
                                 "right": "entrance_hallway_right"},["dollar"])
space_list["entrance_hallway_left"] = space("the left hallway, leading to more buildings.",
                                {"forward": "firing_range",
                                 "right": "hallway_3",
                                 "back": "main_room"})
space_list["entrance_hallway_right"] = space("the right entrance hallway, leading to more buildings.",
                                {"forward": "research_building",
                                 "left": "baracks_1",
                                 "back": "main_room"})
space_list["admin_office"] = space("the office for the base. complete with a secretary desk and wilting potted plants. papers have been left scattered over the desk.",

                                     {"left": "entrance_hallway_left",
                                 "right": "entrance_hallway_right",
                                      "back": "main_room"},["token_machine"])
space_list["firing_range"] = space("the indoor firing range. a room with a firing range with multiple guns and dummies with targets. guns are stowed away in compartments, with multiple missing. the dummies have been knocked down. ",
                                   {"right": "hallway_3",
                                 "back":"entrance_hallway_left"})
space_list["hallway_3"] = space("another short hallway that leads to two buildings. forward, a courtyard. right, an exercise area/gym.",
                                 {"forward": "courtyard",
                                  "right": "exercise_area",
                                 "back":"hallway_4"})
space_list["courtyard"] = space("a building w/ open roof, grass, greenery & tables. ",
                                { "right": "exercise_area",
                                 "back":"hallway_3"})
space_list["exercise_area"] = space("the exercise area. room of exercise machines & equipment, such as treadmills. very dusty. on the right is a hallway.",
                                { "right": "hallway_4",
                                 "left": "courtyard",
                                 "back":"hallway_3"})
space_list["hallway_4"] = space("hallway leading to a cardio room and more hallways w/ rooms.",
                                { "forward": "cardio_room",
                                  "right": "hallway_6",
                                 "left": "hallway_3",
                                  "back": "entrance_hallway_left"})
space_list["hallway_5"] = space("a hallway that leads to the other baracks.",
                                { "forward": "cardio_room",
                                  "back": "hallway_3",
                                  "right": "baracks_2"})
space_list["baracks_1"] = space("baracks. soldiers living quarters. almost all of them are messy with items scattered around rooms, as if people left without their belongings, leaving them where they left them. dusty.",
                                {"back": "hallway_2"})
space_list["baracks_2"] = space("baracks. soldiers living quarters. almost all of them are messy with items scattered around rooms, as if people left without their belongings, leaving them where they left them. dusty.",
                                {"back": "hallway_5"})
space_list["cardio_room"] = space("cardio room. an exercise room, but smaller than the other located in the base. dusty. some weights have been left on the floor. ",
                                { "forward": "hallway_6",
                                  "right":"baracks_2",
                                  "back": "hallway_4"})
space_list["hallway_6"] = space("a hallway past the cardio room that leads to the amory and off into another hallway.",
                                {"right": "amory" ,
                                  "left" : "hallway_7",
                                  "back": "cardio_room"})
space_list["amory"] = space("a room complete with weapons such as different guns. bullets are accross the floor and many guns have been taken or knocked down.",
                                { "back": "hallway_6"})
space_list["hallway_7"] = space("a hallway leading to the pool and a small hallway off to the side.",
                                { "forward": "pool",
                                  "back": "hallway_6",
                                  "right": "hallway_8"})
space_list["research_building"] = space("research building. a white room full of scientific/medical equipment and several large cabinets and freezers. everything is dusty but undisturbed. a deafining silence and otherworldly feel accompanies this room. several things have locks, labeled classified.",
                                {  "back": "entrance_hallway_right",
                                  "left": "baracks_1"},["cabinet_with_lock"])
space_list["hallway_8"] = space("a small hallway that leads to the officer quarters and an emergency exit.",
                                {"back": "hallway_7",
                                  "right": "officer_quarters"})
space_list["officer_quarters"] = space("officer quarters. looking almost exactly similar to the state of the baracks, it is messy. there is an emergency exit up forward. it has been left open a crack.",
                                { "forward": "exit",
                                  "back": "hallway_8",
                                  },["video_game"])
space_list["exit"] = space("you have gone through the base and left. ",
                                { "back": "officer_quarters" })
current_room = space_list["main_room"]
def main  ():
    not_done = True
    print current_room.description
    while(not_done):
        input_row = raw_input("What do you want to do? ")
        input_array = input_row.split(" ")
        action = input_array[0]
        if action == "forward" or action == "left" or action == "right" or action == "back":
            current_room.move(action)
        elif action == "pickup":
            if input_array[1] == "dollar":
                pickup_dollar()
        elif action == "put":
            if input_array[1] == "dollar" and input_array[2] == "token" and input_array[3] == "machine":
                put_dollar_token_machine()
        elif action == "play":
            if input_array[1] == "video" and input_array[2] == "game":
                play_video_game()
        elif action == "look":
            print current_room.description
            print "items:{0}".format(current_room.get_items())
        elif action == "inventory":
            print "Inventory:{0}".format(inventory)
        elif action == "type" and input_array [1] == "keypad" and len (input_array) == 6:
            enter_combination(input_array[2],input_array[3],input_array[4],input_array[5])
        elif action == "read" and input_array[1] == "clue":
            read_clue()
        elif action == "read" and input_array[1] == "logbook":
            read_logbook()
        elif action == "go":
            go_to_room(input_array[1])
        else:
            print "I don't understand {0}".format(action)



if __name__ == "__main__":
    main ()
