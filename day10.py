from aocd import data, get_data


#load data
data = get_data(day=10, year=2022)
data = data.split('\n')

cycle, X, XsSum = 0, 1, 0

#check X during** the cycles, so when the 20th cycle has not yet completed...
def checkState():
    global XsSum
    if cycle in [20, 60, 100, 140, 180, 220]:
        XsSum += X*cycle


data.reverse()

def processCommand(command):
    global X
    global cycle
    if 'noop' in command:
        #nothing happens
        pass
    else:
        cycle += 1 
        checkState()
        num = int(command.split(' ')[1])
        X += num

while data:
    curr = data.pop()

    cycle += 1
    checkState()

    processCommand(curr)

#part 1 answer...
print(XsSum)


#part 2...

