state = "......####..##.##..##..#..###..#....#.######..###########.#...#.##..####.###.#.###.###..#.####..#.#..##..#......"
notes = {
    ".#.## => .",
    "...## => #",
    "..#.. => .",
    "#.#.. => .",
    "...#. => .",
    ".#... => #",
    "..... => .",
    "#.... => .",
    "#...# => #",
    "###.# => .",
    "..### => #",
    "###.. => .",
    "##.## => .",
    "##.#. => #",
    "..#.# => #",
    ".###. => .",
    ".#.#. => .",
    ".##.. => #",
    ".#### => .",
    "##... => .",
    "##### => .",
    "..##. => .",
    "#.##. => .",
    ".#..# => #",
    "##..# => .",
    "#.#.# => #",
    "#.### => .",
    "....# => .",
    "#..#. => #",
    "#..## => .",
    "####. => #",
    ".##.# => #"
}

begin_pot = 6

print("state: ", state)
for i in range(80000000000):
    print(i)
    # extend amount of pots
    first = state.find("#")
    last = state.rfind("#")
    temp_pot = begin_pot
    if last > (len(state) - 6):
        state += "." * (7 - (len(state) - last))
    if (first - 6) < 0:
        state = "." * (abs(first - 6)) + state
        begin_pot += abs(first - 6)
    # print("State: ", state)
    state_list = list(state)
    # print("begin_pot: ", temp_pot, " end begin_pot: ", begin_pot)
    state = ""
    # print("iter: ", i)
    # print("state: ", state_list)
    for pot in range(first - 4, last + 4, 1):
        # get pot sequence
        pot_check = state_list[pot - 2] + state_list[pot - 1] + state_list[pot] \
            + state_list[pot + 1] + state_list[pot + 2]

        # print("pot_check: ", pot_check)
        # check sequence against notes
        for note in notes:
            if note[:5] == pot_check:
                # print("note: ", note[:5], " pot_check: ", pot_check)
                state += note[9]
                break
    state = "." * 2 + state + "." * 2
    # print("state: ", state)
total = 0
for pot in range(len(state)):
    if state[pot] == '#':
        total += (pot - begin_pot)
print("state: ", state, " Sum: ", state.count('#'), " : ", total)
#3230