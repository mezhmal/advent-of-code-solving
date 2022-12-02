rock = 1
paper = 2
scissors = 3

lose = 0
draw = 3
win = 6

combination_score_map = {
    'A X': rock + draw,      # (A) rock : rock => draw
    'A Y': paper + win,      # (A) rock : paper => win
    'A Z': scissors + lose,  # (A) rock : scissors => loss
    'B X': rock + lose,      # (B) paper : rock => loss
    'B Y': paper + draw,     # (B) paper : paper => draw
    'B Z': scissors + win,   # (B) paper : scissors => win
    'C X': rock + win,       # (C) scissors : rock => win
    'C Y': paper + lose,     # (C) scissors : paper => loss
    'C Z': scissors + draw,  # (C) scissors : scissors => draw
}

combination_score_map_2 = {
    'A X': scissors + lose,  # (A) rock : scissors => (X) lose
    'A Y': rock + draw,  # (A) rock : rock => (Y) draw
    'A Z': paper + win,  # (A) rock : paper => (Z) win
    'B X': rock + lose,  # (B) paper : rock => (X) lose
    'B Y': paper + draw,  # (B) paper : paper => (Y) draw
    'B Z': scissors + win,  # (B) paper : scissors => (Z) win
    'C X': paper + lose,  # (C) scissors : paper => (X) lose
    'C Y': scissors + draw,  # (C) scissors : scissors => (Y) draw
    'C Z': rock + win,  # (C) scissors : rock => (Z) win
}

scores = []
scores2 = []

with open('input.txt') as f:
    for line in f.readlines():
        scores.append(combination_score_map.get(line.strip(), 0))
        scores2.append(combination_score_map_2.get(line.strip(), 0))

print(f"Total score: {sum(scores)}")
print(f"Total score 2: {sum(scores2)}")
