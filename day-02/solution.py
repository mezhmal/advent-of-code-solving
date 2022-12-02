combination_score_map = {
    'A X': 1 + 3,  # rock : rock => draw
    'A Y': 2 + 6,  # rock : paper => win
    'A Z': 3 + 0,  # rock : scissors => loss
    'B X': 1 + 0,  # paper : rock => loss
    'B Y': 2 + 3,  # paper : paper => draw
    'B Z': 3 + 6,  # paper : scissors => win
    'C X': 1 + 6,  # scissors : rock => win
    'C Y': 2 + 0,  # scissors : paper => loss
    'C Z': 3 + 3,  # scissors : scissors => draw
}

scores = []
with open('input.txt') as f:
    for line in f.readlines():
        scores.append(combination_score_map.get(line.strip(), 0))

print(f"Total score: {sum(scores)}")