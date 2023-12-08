cards = open("day4.txt",'r').read().split("\n")

score = 0
for card in cards:
    winning,own = card[len("Card   1: "):].split("|")
    winning = {int(elem) for elem in winning.strip().split(" ") if elem != ''}
    own = {int(elem) for elem in own.strip().split(" ") if elem != ''}
    num_matches = len(winning.intersection(own))
    if num_matches > 0:
        score += (2**(num_matches-1))


copies = list(range(len(cards)))
assert len(copies) == 214
for card in cards:
    winning,own = card[len("Card   1: "):].split("|")
    winning = {int(elem) for elem in winning.strip().split(" ") if elem != ''}
    own = {int(elem) for elem in own.strip().split(" ") if elem != ''}
    num_matches = len(winning.intersection(own))
    

