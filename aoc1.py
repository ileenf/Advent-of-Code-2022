import heapq
def calorie_counting(path):
    file = open(path)

    max_calories = -1
    curr_count = 0
    for line in file:
        line = line.strip()

        if line == '':
            max_calories = max(max_calories, curr_count)
            curr_count = 0
        else:
            curr_count += int(line)

    return max_calories

def calorie_counting2(path):
    file = open(path)

    max_three_calories = [-1, -1, -1]
    heapq.heapify(max_three_calories)

    curr_count = 0
    for line in file:
        line = line.strip()

        if line == '':
            top_three_min = heapq.heappop(max_three_calories)
            if curr_count > top_three_min:
                heapq.heappush(max_three_calories, curr_count)
            else:
                heapq.heappush(max_three_calories, top_three_min)
            curr_count = 0
        else:
            curr_count += int(line)

    return sum(max_three_calories)

print(calorie_counting2('aoc1.txt'))

