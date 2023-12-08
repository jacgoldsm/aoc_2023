red = 12
green = 13
blue = 14

text = open("day2.txt", "r").read().split("\n")


acc = 0
import re
for line in text:
    valid = True
    id_ = int(re.findall("Game ([0-9]+)", line)[0])
    line = re.sub("Game [0-9]+: ", "", line)
    split = line.split(";")
    split = [s.split(",") for s in split]
    split = [item.strip() for sublist in split for item in sublist]
    for elem in split:
        num = int("".join([e for e in elem if e.isdigit()]))
        color = "".join([e for e in elem if e.isalpha()])
        if color == "red":
            if num > red:
                valid = False
        elif color == "green":
            if num > green:
                valid = False
        elif color == "blue":
            if num > blue:
                valid = False
        else:
            raise AssertionError(f"Color is {color}, invalid")
    if valid:
        acc += id_

    #print(num,"TRUE" if valid else "FALSE")

#print(acc)


acc = 0
import re
for line in text:
    valid = True
    id_ = int(re.findall("Game ([0-9]+)", line)[0])
    line = re.sub("Game [0-9]+: ", "", line)
    split = line.split(";")
    split = [s.split(",") for s in split]
    split = [item.strip() for sublist in split for item in sublist]
    reds,greens,blues = set(),set(),set()
    for elem in split:
        num = int("".join([e for e in elem if e.isdigit()]))
        color = "".join([e for e in elem if e.isalpha()])
        if color == "red":
            reds.add(num)
        elif color == "green":
            greens.add(num)
        elif color == "blue":
            blues.add(num)
        else:
            raise AssertionError(f"Color is {color}, invalid")
    acc += max(reds) * max(greens) * max(blues)

print(acc)
