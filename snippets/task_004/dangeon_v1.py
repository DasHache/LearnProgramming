print "L0: You are on the ground."
print "L0: Descending to the level 1..."
level = 1

if level == 1:

    print "\tL1: You are on level 1"
    print "\tL1: Here is your Water magic"
    water = 100
    print "\tL1: water = ", water

    print "\tL1: Now you can use Water!"
    print "\tL1: Descending..."
    level = 2

    if level == 2: 

        print "\t\tL2: You are on level 2"
        print "\t\tL2: Here is your Fire magic"
        fire = 200
        print "\t\tL2: water = ", water
        print "\t\tL2: fire  = ", fire
        
        print "\t\tL2: Now you can use Water and Fire!"
        print "\t\tL2: Descending..."
        level = 3

        if level == 3:
            print "\t\t\tL3: You are on level 3"
            print "\t\t\tL3: Here is your Air magic"
            air = 300
            print "\t\t\tL3: water = ", water
            print "\t\t\tL3: fire  = ", fire
            print "\t\t\tL3: air = ", air
            
            print "\t\t\tL3: Now you can use Water, Fire and Air!"
            print "\t\t\tL3: Killing the bad guy..."
            print "\t\t\tL3: Done. Ascending to level 2..."

        print "\t\tL2: Here, you are back on level 2."
        print "\t\tL2: Have you noticed the changes in the identation?"
        print "\t\tL2: Identation is the number of empty space before the line of code"
        print "\t\tL2: Remember, you have LOST you Air spell!"
        print "\t\tL2: However, you still have Water and Fire."
        print "\t\tL2: water = ", water
        print "\t\tL2: fire  = ", fire
        print "\t\tL2: air   = ", air  # it is NOT an ERROR here!?...................
        print "\t\tL2: Ascending to level 1..."

    print "\tL1: Here, you are back on level 1."
    print "\tL1: Just one 'tab' of identation."
    print "\tL1: Remember, you have LOST you Fire!"
    print "\tL1: Only Water is valid here."
    print "\tL1: Exiting level 1..."

print "L0: Here, you are back to the town."
print "L0: No spaces before 'print'."
print "L0: No more magic."
print "L0: But you are a hero!"
