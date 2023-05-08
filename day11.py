from aocd import data, get_data


class Monkey:
  def __init__(self, starting_items, operation, test):
    self.starting_items = starting_items
    self.operation = operation
    self.test = test
    self.inspections = 0

#load data
data = get_data(day=11, year=2022)
data = data.split('\n')

monkey_dict, monkey = {}, 0
test = []
operation = []

for line in data:
    if 'items' in line:
        index = line.find(':')
        line_truncated = line[index+1:]
        worry_nums = line_truncated.split(',')
        starting_items = map(lambda x: int(x), worry_nums)


    elif 'Test' in line:
        line = line.split(' ')
        test.append(int(line[-1]))

    elif 'true' in line:
        line = line.split(' ')
        test.append(int(line[-1]))
        
    elif 'false' in line:
        line = line.split(' ')
        test.append(int(line[-1]))

    elif 'Operation' in line:
        operation = line.split(' ')

    if operation and len(test) == 3 and starting_items:
        monkey_dict[monkey] = Monkey(list(starting_items), operation, test)
        starting_items, operation, test = [], [], []
        monkey += 1

for _ in range(20):
    for monkey in monkey_dict:
        while monkey_dict[monkey].starting_items:
            monkey_dict[monkey].inspections += 1
            item = monkey_dict[monkey].starting_items.pop(0)
            num, operation = monkey_dict[monkey].operation[-1], monkey_dict[monkey].operation[-2]
            test = monkey_dict[monkey].test 
            
            if operation == '*':
                if num != 'old':
                    item = item * int(num)
                else:
                    item = item * item
            elif operation == '+':
                item = item + int(num)

            #divided item worry level by 3
            item = item // 3

            #test item to determine which monkey it goes to next
            if item % test[0] == 0:
                monkey_dict[test[1]].starting_items.append(item)

            else:
                monkey_dict[test[2]].starting_items.append(item)


freq = []
for monkey in monkey_dict:
    freq.append(monkey_dict[monkey].inspections)


freq.sort()

#part 1 answer...
print(freq[-1] * freq[-2])




            



    













    
    
