from aocd import data, get_data


#load data
data = get_data(day=3, year=2022)

rucksacks = data.split('\n')
priorities_sum = 0
priority_dict = {chr(i): i-96 for i in range(97, 123)}
priority_dict.update({chr(i): i-38 for i in range(65, 91)})


def findBothCompartmentLetter(ruckstack):

    n = len(ruckstack) // 2

    first_half, second_half = set(ruckstack[:n]), set(ruckstack[n:])
    overLappingLetter = first_half & second_half

    if len(overLappingLetter) != 1:
        raise Exception("bad input")

    return overLappingLetter.pop()


for backpack in rucksacks:
    priorities_sum += priority_dict[findBothCompartmentLetter(backpack)]


#part 1 answer
print(priorities_sum)


#part 2 answer

def findGroupBadge(elfPacks):
    #trim last ',' from string
    elfPacks = elfPacks[:-1]
    
    packArr = elfPacks.split(',')
    a, b, c = packArr
    a, b, c = set(a), set(b), set(c)

    overLap = a & b & c 

    if len(overLap) != 1:
        raise Exception("bad input")
    
    return overLap.pop()

elf_count = 0
elfPacks = ''
priorities_sum = 0
for backpack in rucksacks:
    elf_count += 1
    elfPacks += backpack + ','
    if elf_count % 3 == 0:
        priorities_sum += priority_dict[findGroupBadge(elfPacks)]
        elf_count = 0 
        elfPacks = ''

#part 2 answer
print(priorities_sum)



