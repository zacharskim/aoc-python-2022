from aocd import data, get_data


#load data
#data = get_data(day=9, year=2022)


#data = 'R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2'
data = 'R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20'

data = data.split('\n')
headRelation = ''
visited = set()

def contact(h, t):

    hr, hc = h
    tr, tc = t 

    if hr == tr and hc == tc:
        return "Same location"

    elif hr == tr:
        return "Same row"

    elif hc == tc:
        return "Same column"

    elif hr + 1 == tr and hc + 1 == tc:
        return 'Top right'

    elif hr + 1 == tr and hc - 1 == tc:
        return 'Top left'

    elif hr - 1 == tr and hc - 1 == tc:
        return 'Bottom left'

    elif hr - 1 == tr and hc + 1 == tc:
        return 'Bottom right'


def move(h, t, dir):
    global head
    global headRelation
    print('head start', h)
    hr, hc = h
   
    if dir == 'R':
        hc += 1
    
    elif dir == 'L':
        hc -= 1

    elif dir == 'U':
        hr += 1

    elif dir == 'D':
        hr -= 1

    head = [hr, hc]
    print('head finish', head)
    headRelation = contact(h, t)

def diagnoallyTouching(h,t):
    hr, hc = h
    tr, tc = t

    if hr == tr and hc == tc:
        return True
    
    elif hr - 1 == tr and hc == tc:
        return True

    elif hr + 1 == tr and hc == tc:
        return True

    elif hr == tr and hc - 1 == tc:
        return True

    elif hr == tr and hc + 1 == tc:
        return True

    elif hr + 1 == tr and hc + 1 == tc:
        return True

    elif hr + 1 == tr and hc - 1 == tc:
        return True

    elif hr - 1 == tr and hc - 1 == tc:
        return True

    elif hr - 1 == tr and hc + 1 == tc:
        return True
    
    else:
        return False



dirs = {'R': 1, 'L': -1, 'U': 1, 'D': -1}
def moveTail(h, t, dir):
    global tail
    global headRelation
    hr, hc = h
    tr, tc = t
    #t is touching h...
    print('movetail', h, t)
    if diagnoallyTouching(h,t):
        print('not moving tail...')
        headRelation = contact(h, t)
        print(headRelation)
        return

    else:
       
        if headRelation == 'Same location':
            return
        elif headRelation == 'Same row':
            if dir == 'R' or dir == 'L':
                tc += dirs[dir]
          
        elif headRelation == 'Same column':
            if dir == 'U' or dir == 'D':
                tr += dirs[dir]

        elif headRelation == 'Top right':
            if dir == 'R':
                pass
            elif dir == 'U':
                pass
            elif dir == 'D' or dir == 'L':
                tr -= 1
                tc -= 1
            
        elif headRelation == 'Top left':
            if dir == 'R':
                tr -=1 
                tc += 1
            elif dir == 'L':
                pass
            elif dir == 'D':
                tr -= 1
                tc += 1
            elif dir == 'U':
                pass

        elif headRelation == 'Bottom right':
            if dir == 'R':
                pass
            elif dir == 'L':
                tr += 1
                tc -= 1
            elif dir == 'D':
               pass
            elif dir == 'U':
                tr += 1
                tc -= 1
            
        elif headRelation == 'Bottom left':
            if dir == 'R':
                tr += 1
                tc += 1
            elif dir == 'L':
                pass
            elif dir == 'D':
               pass
            elif dir == 'U':
                tr += 1
                tc += 1
        
        tail = [tr, tc]
        visited.add((tr,tc))
        print('new tail', tail)


visited.add((0,0))

head, tail = [0,0], [0,0]
for movement in data:
    dir, num = movement.split(' ')
    for _ in range(int(num)):
        move(head, tail, dir)
        moveTail(head,tail, dir)

#part 1 answer
print(len(visited))


#part 2
head, tail = [0,0], [0,0]
for movement in data:
    dir, num = movement.split(' ')
    for _ in range(int(num)):
        move(head, tail, dir)
        moveTail(head,tail, dir)

