text = open("day3.txt", 'r').read()

lines = text.split("\n")

part2 = True
out: dict[tuple[int],str] = {}
for i,line in enumerate(lines):
    for j,elem in enumerate(line):
        out[(i,j)] = elem

for idx in range(140):
    out[(idx,140)] = '.'

symbols = {elem for elem in text if not elem.isalnum() and elem not in ('.','\n')}
if part2:
    symbols = ("*")
print(symbols)

i,j = 0,0
nums = dict()
syms = set()
while i < 140:
    if out[(i,j)].isdigit():
        digits = []
        col = j
        while out[(i,j)].isdigit():
            digits.append(out[(i,j)])
            j += 1
        nums[(i,col,j-1)] = int("".join(digits))
    
    if out[(i,j)] in symbols:
        syms.add((i,j))
    if j < 139:
        j += 1
    else:
        i += 1
        j = 0

acc = 0
for i,start,end in nums.keys():
    adjacent = False
    if (i,start-1) in syms or (i,end+1) in syms:
        adjacent = True
    elif any((i-1,col) in syms for col in range(start-1,end+2)):
        adjacent = True
    elif any((i+1,col) in syms for col in range(start-1,end+2)):
        adjacent = True
    if adjacent:
        acc += nums[(i,start,end)]
    else:
        pass

#print(acc)

# part 2

def is_adjacent(sym,num):
    n_row,n_start,n_end = num
    s_row,s_col = sym
    if abs(n_row - s_row) <= 1:
        if abs(n_end - s_col) <= 1 or abs(n_start - s_col) <= 1:
            return True
        if n_start <= s_col and n_end >= s_col:
            return True
    return False
p2_acc = 0
for s in syms:
    adjacents = [nums[elem] for elem in nums.keys() if is_adjacent(s,elem)]
    if len(adjacents) == 2:
        p2_acc += adjacents[0] * adjacents[1]

print(p2_acc)