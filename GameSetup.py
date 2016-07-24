
def setup(Hex, itertools, random):
    #(roll, number of dots, 8or6 = 1)


    while True:
        conflict = 0
        rolls = [(2, 1, 0), (3, 2, 0), (3, 2, 0), (4, 3, 0), (4, 3, 0), (5, 4, 0), (5, 4, 0), (6, 5, 1), (6, 5, 1),
                 (8, 5, 1), (8, 5, 1), (9, 4, 0), (9, 4, 0), (10, 3, 0), (10, 3, 0), (11, 2, 0), (11, 2, 0), (12, 1, 0)]
        location = [(0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2), (1, 3),
                    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                    (3, 0), (3, 1), (3, 2), (3, 3),
                    (4, 0), (4, 1), (4, 2)]
        random.shuffle(rolls)
        random.shuffle(location)

        hexes = [[Hex("Brick", rolls.pop(), location.pop())],
                 [Hex("Brick", rolls.pop(), location.pop())],
                 [Hex("Brick", rolls.pop(), location.pop())],
                 [Hex("Ore", rolls.pop(), location.pop())],
                 [Hex("Ore", rolls.pop(), location.pop())],
                 [Hex("Ore", rolls.pop(), location.pop())],
                 [Hex("Lumber", rolls.pop(), location.pop())],
                 [Hex("Lumber", rolls.pop(), location.pop())],
                 [Hex("Lumber", rolls.pop(), location.pop())],
                 [Hex("Lumber", rolls.pop(), location.pop())],
                 [Hex("Wool", rolls.pop(), location.pop())],
                 [Hex("Wool", rolls.pop(), location.pop())],
                 [Hex("Wool", rolls.pop(), location.pop())],
                 [Hex("Wool", rolls.pop(), location.pop())],
                 [Hex("Grain", rolls.pop(), location.pop())],
                 [Hex("Grain", rolls.pop(), location.pop())],
                 [Hex("Grain", rolls.pop(), location.pop())],
                 [Hex("Grain", rolls.pop(), location.pop())],
                 1 * [Hex("Desert", (0, 0, 0), location.pop())],
                 ]


        hex_array = list(itertools.chain.from_iterable(hexes))
        #random.shuffle(pod)

        red_array = []
        for i in range(len(hex_array)):
            #print "Resource, Values, Location: ", hex_array[i].getResource(), hex_array[i].getValue(), hex_array[i].getLocation()
            if (hex_array[i].getValue()[2] == 1):
                red_array.append(i)

        for i in range(0, 3):
            for j in range(i+1, 4):
                diff1 = hex_array[red_array[i]].getLocation()[0] - hex_array[red_array[j]].getLocation()[0]
                diff2 = hex_array[red_array[i]].getLocation()[1] - hex_array[red_array[j]].getLocation()[1]
                if ((abs(diff1) < 2) and (abs(diff2) < 2)):
                    #print "Conflict between: ", hex_array[red_array[i]].getLocation(), " and ", hex_array[red_array[j]].getLocation()
                    conflict = 1

        if (conflict == 0):
            #print "Found configuration!"
            #for i in range(4):
                #print hex_array[red_array[i]].getLocation()
            break

    return


