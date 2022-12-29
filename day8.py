from aocd import data, get_data


#load data
data = get_data(day=8, year=2022)


#data = '30373\n25512\n65332\n33549\n35390'

data = data.split('\n')

rows, cols = len(data), len(data[0])


def visible(r, c):
    #A tree is visible if all of the other trees between it and an edge of the grid are shorter than it
    #only need to be visible in one direction to be visible
    height = data[r][c]
    #up
    R = r
    while R >= 0:
        R -= 1
        if height <= data[R][c]:
            break
    
        if R == 0:
            return True
    #down
    R = r
    while R < rows:
        R += 1
        if height <= data[R][c]:
            break

        if R == rows-1:
            return True
    #left 
    C = c
    while C >= 0:
        C -= 1
        if height <= data[r][C]:
            break

        if C == 0:
            return True
    #right
    C = c
    while C < cols:
        C += 1
        if height <= data[r][C]:
            break

        if C == cols-1:
            return True

    #if not visible in any direction, tree is not visible...
    return False

    



edgeTrees = 0
for r in range(rows):
    for c in range(cols):
        if c == 0 or r == 0 or c == cols - 1 or r == rows - 1:
            edgeTrees += 1
        

#only concerned with inner trees now...
visibleTrees = 0
for r in range(1,rows-1):
    for c in range(1, cols-1):
        if visible(r,c):
            visibleTrees += 1

#part 1 answer
print(visibleTrees + edgeTrees)


#part 2

#tweak visible function to calculate senic scores
def senicScore(r,c):

    height = data[r][c]
    #up
    R = r
    u_score = 0
    while R > 0:
        R -= 1
        u_score += 1
        if height <= data[R][c]:
            break
    
        if R == 0:
            break
    #down
    R = r
    d_score = 0
    while R < rows-1:
        R += 1
        d_score += 1
        if height <= data[R][c]:
            break

        if R == rows-1:
            break
    #left 
    C = c
    l_score = 0
    while C > 0:
        C -= 1
        l_score += 1
        if height <= data[r][C]:
            break

        if C == 0:
            break
    #right
    C = c
    r_score = 0
    while C < cols - 1:
        C += 1
        r_score += 1
        if height <= data[r][C]:
            break

        if C == cols-1:
            break

    return u_score * d_score * r_score * l_score

m_senic_val = float('-inf')
for r in range(rows):
    for c in range(cols):
        senic_val = senicScore(r,c)

        if senic_val > m_senic_val:
            m_senic_val = senic_val

#part 2 answer
print(m_senic_val)




