from aocd import data, get_data


#load data
data = get_data(day=6, year=2022)



for i in range(len(data)-4):
    marker = data[i:i+4]
    
    if len(marker) == len(set(marker)):
        #part 1 answer
        print(i+4)
        break


for i in range(len(data)-14):
    marker = data[i:i+14]

    if len(marker) == len(set(marker)):
        #part 2 answer
        print(i+14)
        break
        

