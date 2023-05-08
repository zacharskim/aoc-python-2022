from aocd import data, get_data

#load data
data = get_data(day=12, year=2022)
data = data.split('\n')





# test = 'Sabqponm, abcryxxl, accszExk, acctuvwj, abdefghi'
# test = test.split(', ')


graph = []
for row in data:
    newRow = []
    for i in range(len(row)):
        if row[i] == 'E':
            newRow.append(123)
        else:
            newRow.append(ord(row[i]))
    graph.append(newRow)
    

rows, cols = len(graph), len(graph[0])


def bfs(graph, start_row, start_col):
    # Initialize the queue with the starting position and a depth of 0
    queue = [(start_row, start_col, 0)]
    visited = []

    # Explore the neighbors of each position in the queue
    while queue:
        row, col, depth = queue.pop(0)

        
        # Check if the current position is out of bounds or is not a 1
        if row < 0 or col < 0 or row >= len(graph) or col >= len(graph[0]) or (row, col) in visited:
            continue

        if graph[row][col] == 123:
            return depth - 2 #-2 for the start and ending nodes i think?
        
        visited.append((row, col))

        neis_to_explore = []
        for nei in [(row - 1, col, depth + 1), (row + 1, col, depth + 1), (row, col - 1, depth + 1), (row, col + 1, depth + 1)]:
            r,c, _ = nei

            if r < 0 or c < 0 or r >= len(graph) or c >= len(graph[0]):
                continue
          
            if graph[r][c] - graph[row][col] <= 1  or graph[row][col] == ord('S'):
                neis_to_explore.append(nei)
            elif graph[row][col] > graph[r][c] and graph[row][col] <= graph[r][c]:
                neis_to_explore.append(nei)

        queue.extend(neis_to_explore)

    
for r in range(rows):
    for c in range(cols):
        if graph[r][c] == ord("S"):
            start_r, start_c = r, c

#part 1 answer
print(bfs(graph=graph, start_row=start_r, start_col=start_c))
