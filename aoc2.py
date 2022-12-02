def rock_paper_scissors(path):
    file = open(path)

    round_outcomes = {'A': {'X': 3, 'Y': 6, 'Z': 0},
                      'B': {'X': 0, 'Y': 3, 'Z': 6},
                      'C': {'X': 6, 'Y': 0, 'Z': 3}}

    shape_to_score = {'X': 1, 'Y': 2, 'Z': 3}
    total_score = 0

    for line in file:
        line = line.strip()
        opponent, curr_player = line.split()

        round_score = round_outcomes[opponent][curr_player]
        shape_score = shape_to_score[curr_player]

        total_score += (round_score + shape_score)

    return total_score

def rock_paper_scissors2(path):
    file = open(path)

    move_to_make = {'A': {'X': 'scissors', 'Y': 'rock', 'Z': 'paper'},
                    'B': {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'},
                    'C': {'X': 'paper', 'Y': 'scissors', 'Z': 'rock'}}

    shape_to_score = {'rock': 1, 'paper': 2, 'scissors': 3}
    round_outcome = {'X': 0, 'Y': 3, 'Z': 6}
    total_score = 0

    for line in file:
        line = line.strip()
        opponent, game_status = line.split()

        move = move_to_make[opponent][game_status]
        shape_score = shape_to_score[move]
        round_score = round_outcome[game_status]

        total_score += (round_score + shape_score)

    return total_score

print(rock_paper_scissors2('aoc2.txt'))

