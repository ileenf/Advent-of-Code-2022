def get_common_char(s1, s2):
    for ch in s1:
        if ch in s2:
            return ch

def rucksack(path):
    file = open(path)
    total = 0

    for line in file:
        line = line.strip()
        length = len(line) // 2

        first_half = line[:length]
        second_half = line[length:]

        common_char = get_common_char(first_half, second_half)

        if common_char.lower() == common_char:
            val = ord(common_char) - ord('a') + 1
        else:
            val = ord(common_char) - ord('A') + 27
        total += val

    return total

def get_common_char(s1, s2, s3):
    for ch in s1:
        if ch in s2 and ch in s3:
            return ch

def calc_badge_score(group):
    common_char = get_common_char(group[0], group[1], group[2])
    if common_char.lower() == common_char:
        val = ord(common_char) - ord('a') + 1
    else:
        val = ord(common_char) - ord('A') + 27
    return val

def rucksack2(path):
    file = open(path)
    total = 0

    group = []
    for line in file:
        if len(group) == 3:
            total += calc_badge_score(group)
            group = [line]
        else:
            group.append(line.strip())

    if group:
        total += calc_badge_score(group)

    return total

print(rucksack2('aoc3.txt'))



