def to_level_1():
    print "\tL1: You are on level 1"
    print "\tL1: Here is your Water magic"
    water = 100
    print "\tL1: water = ", water

    print "\tL1: Now you can use Water!"
    print "\tL1: Descending?... (press Enter)"
    raw_input()

    to_level_2(water)

    print "\tL1: Here, you are back on level 1."
    print "\tL1: Just one 'tab' of identation."
    print "\tL1: Remember, you have LOST you Fire!"
    print "\tL1: Only Water is valid here."
    print "\tL1: Exiting level 1... (press Enter)"
    raw_input()


def to_level_2(water):
    print "\t\tL2: You are on level 2"
    print "\t\tL2: Here is your Fire magic"
    fire = 200
    print "\t\tL2: water = ", water
    print "\t\tL2: fire  = ", fire
    
    print "\t\tL2: Now you can use Water and Fire!"
    print "\t\tL2: Descending... (press Enter)"
    raw_input()

    to_level_3(water, fire)

    print "\t\tL2: Here, you are back on level 2."
    print "\t\tL2: Have you noticed the changes in the identation?"
    print "\t\tL2: Identation is the number of empty space before the line of code"
    print "\t\tL2: Remember, you have LOST you Air spell!"
    print "\t\tL2: However, you still have Water and Fire."
    print "\t\tL2: water = ", water
    print "\t\tL2: fire  = ", fire
    #print "\t\tL2: air   = ", air  # UNCOMMENT this line to see the ERROR
    print "\t\tL2: Ascending to level 1... (press Enter)"
    raw_input()

def to_level_3(water, fire):
    print "\t\t\tL3: You are on level 3"
    print "\t\t\tL3: Here is your Air magic"
    air = 300
    print "\t\t\tL3: water = ", water
    print "\t\t\tL3: fire  = ", fire
    print "\t\t\tL3: air = ", air
    
    print "\t\t\tL3: Now you can use Water, Fire and Air!"
    print "\t\t\tL3: Killing the bad guy..."
    print "\t\t\tL3: Done. Ascending to level 2... (press Enter)"
    raw_input()
