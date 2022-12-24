from aocd import data, get_data

#load data
data = get_data(day=1, year=2022)

#split input into arr with each element representing an elf
elf_data = data.split('\n\n')

elf_cal_sums = []
for elf in elf_data:
    elf_cals = elf.split('\n')
    elf_cals_ints = [int(s) for s in elf_cals]
    elf_cal_sums.append(sum(elf_cals_ints))


#part 1 answer - what's the highest amount of calories carried by a single elf?
print(max(elf_cal_sums))


#part 2 answer - what's the total sum of the top three highest calories carrying elfs? 
elf_cal_sums.sort()

print(sum(elf_cal_sums[-3:]))
