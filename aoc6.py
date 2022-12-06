def tuning(path, marker):
    with open(path) as file:
        for line in file:
            line = line.strip()

    for i in range(len(line)-marker):
        seen_chars = set()
        for j in range(i, i+marker):
            seen_chars.add(line[j])
        if len(seen_chars) == marker:
            return j+1


print(tuning('aoc6.txt', 4))


