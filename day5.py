from aocd import data, get_data
import re


#load and clean data
data = get_data(day=5, year=2022)


crates, instructions = data.split('\n\n')

crates = crates.split('\n')
rows, cols = len(crates), len(crates[0])
instructions = instructions.split('\n')

crates_clean = []
for c in range(cols):
    stack = []
    for r in range(rows):
        if crates[r][c].isalpha():
            stack.append(crates[r][c])

        elif crates[r][c].isdigit():
            stack.reverse()
            crates_clean.append(stack)
            stack = []




def moveCrate(instruction):

    num_crates, From, to = [int(s) for s in instruction.split() if s.isdigit()]


    while num_crates:
        if crates_clean[From-1]:
            crate = crates_clean[From-1].pop()
            crates_clean[to-1].append(crate)
        
        num_crates -= 1

    

for instruction in instructions:
    moveCrate(instruction)


ans = ''
for crate_stack in crates_clean:
    if crate_stack:
        ans += crate_stack.pop()

#part 1 answer
print(ans)



#part 2 answer
data = get_data(day=5, year=2022)


crates, instructions = data.split('\n\n')

crates = crates.split('\n')
rows, cols = len(crates), len(crates[0])
instructions = instructions.split('\n')

crates_clean = []
for c in range(cols):
    stack = []
    for r in range(rows):
        if crates[r][c].isalpha():
            stack.append(crates[r][c])

        elif crates[r][c].isdigit():
            stack.reverse()
            crates_clean.append(stack)
            stack = []

def moveCrates(instruction):

    num_crates, From, to = [int(s) for s in instruction.split() if s.isdigit()]

    crates = []
    while num_crates:
        if crates_clean[From-1]:
            crates +=  [crates_clean[From-1].pop()]
            
        num_crates -= 1
    
    crates.reverse()
    crates_clean[to-1].extend(crates)


moveCrates("move 3 from 8 to 3")


for instruction in instructions:
    moveCrates(instruction)


ans = ''
for crate_stack in crates_clean:
    if crate_stack:
        ans += crate_stack.pop()

print(ans)