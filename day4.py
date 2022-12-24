from aocd import data, get_data


#load data
data = get_data(day=4, year=2022)


cleaning_assignment_pairs = data.split('\n')

def findFullOverLap(pairs):
    
    #split string into array of two numbers then check if numbers overlap fully
    elf1, elf2 = pairs.split(',')
    elf1, elf2 = elf1.split('-'), elf2.split('-')

    a,b = int(elf1[0]), int(elf1[1])
    c,d = int(elf2[0]), int(elf2[1])

    if a <= c and b >= d:
        return 1
    
    elif a >= c and b <= d:
        return 1

    else:
        return 0 

full_overlap_count = 0
for assignment in cleaning_assignment_pairs:
    full_overlap_count += findFullOverLap(assignment)

#part 1 answer
print(full_overlap_count)

#part 2 answer

def findOverLap(pairs):
    
    #split string into array of two numbers then check if numbers overlap
    elf1, elf2 = pairs.split(',')
    elf1, elf2 = elf1.split('-'), elf2.split('-')

    a,b = int(elf1[0]), int(elf1[1])
    c,d = int(elf2[0]), int(elf2[1])

    if a <= d and b >= c:
        return 1 
    
    else:
        return 0 

overlap_count = 0
for assignment in cleaning_assignment_pairs:
    overlap_count += findOverLap(assignment)

#part 2 answer
print(overlap_count)


