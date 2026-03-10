def tournament_winner(competitions, results):
    scores = {} # set a dictionary to store each team's score
    current_winner = "" # keeps track of which team is in the lead
    scores[current_winner] = 0 # initialise to 0
    match_winner = "" # set match winner variable

    for competition, result in zip(competitions, results): # pair each competition with its result
        home, away = competition # split competition into home and away
        # determine match winner
        if result == 1:
            match_winner = home
        elif result == 0:
            match_winner = away
        else:
            print("Result should be 0 or 1")

        # add winner and score to scores dictionary
        if match_winner not in scores:
            scores[match_winner] = 0 # initialise to 0
        scores[match_winner] += 3 # add to winner's total

        if scores[match_winner] > scores[current_winner]:
            current_winner = match_winner # update current_winner

    return current_winner # return highest scorer


competitions = [
    ["Panthers", "Lionesses"], # Lionesses win
    ["Lionesses", "Dolphins"], # Dolphins win
    ["Dolphins", "Panthers"] # Dolphins win
]
results = [0, 0, 1]

print(tournament_winner(competitions, results)) # winner - Dolphins






# winner = D
competitions2 = [
    ['A', 'B'],
    ['B', 'C'],
    ['C', 'A'],
    ['D', 'C'],
    ['E', 'D'],
    ['D', 'A'],
]

results2 = [0, 1, 1, 1, 0, 1]

print(tournament_winner(competitions2, results2))


# winner = Lionesses
competitions3 = [
    ['Panthers', 'Lionesses'],
    ['Panthers', 'Dolphins'],
    ['Dolphins', 'Lionesses'],
]

results3 = [0, 0, 0]

print(tournament_winner(competitions3, results3))