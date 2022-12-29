from aocd import data, get_data


#load data
data = get_data(day=7, year=2022)

#data = '$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k'

inputs = data.split('\n')

dirs = {}
filepath = ''

def runCommand(input):
    
    global filepath
    global dirs

    if 'cd ..' in input:
        #go back
        if filepath == '/':
            return
        
        if filepath[-1] == '/':
            filepath = filepath[:-1]
            index = filepath.rfind('/')
            filepath = filepath[:index] + '/'

   
        
    elif 'cd ' in input:
        #make / enter new dir
        dirTitle = input.split(' ')[2]
      
        if dirTitle != '/':
            filepath += dirTitle + '/'
        else:
            filepath = '/'

        if filepath not in dirs:
            dirs[filepath] = 0
        

def processInput(input):
    global dirs
    inputArr = input.split(' ')

    size, title = inputArr[0], inputArr[1]
    if size == 'dir':
        return
    else:
        size = int(size)
        filepathCopy = filepath

        while filepathCopy:    
            if filepathCopy in dirs:
                dirs[filepathCopy] += size

            if filepathCopy == '/':
                break
            if filepathCopy[-1] == '/':
                filepathCopy = filepathCopy[:-1]
                index = filepathCopy.rfind('/')
                filepathCopy = filepathCopy[:index] + '/'
        

for input in inputs:
    if '$' in input:
        runCommand(input)
      
    else:
        processInput(input)

res = 0 
for dir in dirs.values():
    if dir <= 100000:
        res += dir
#part 1 answer
print(res)

#part 2

unusedSpace = 70000000 - dirs['/']

contenders = []
for dir in dirs:
    #if removing a given directory results in an increase of unused spaced greater than or equal to 30000000 we consider it
    if unusedSpace + dirs[dir] >= 30000000:
        contenders.append([dirs[dir], dir])
#part 2 answer
print(sorted(contenders)[0])

