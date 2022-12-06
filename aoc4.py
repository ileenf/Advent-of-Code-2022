def camp_cleanup(path):
    complete_overlap = 0
    with open(path) as file:
        for line in file:
            elf1, elf2 = line.strip().split(',')

            start1, end1 = elf1.split('-')
            start2, end2 = elf2.split('-')

            start1, end1 = int(start1), int(end1)
            start2, end2 = int(start2), int(end2)

            if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
                complete_overlap += 1

    return complete_overlap

def camp_cleanup2(path):
    any_overlap = 0
    with open(path) as file:
        for line in file:
            elf1, elf2 = line.strip().split(',')

            start1, end1 = elf1.split('-')
            start2, end2 = elf2.split('-')

            start1, end1 = int(start1), int(end1)
            start2, end2 = int(start2), int(end2)

            if end1 < start2 or end2 < start1:
                continue
            any_overlap += 1

    return any_overlap

print(camp_cleanup2('aoc4.txt'))


