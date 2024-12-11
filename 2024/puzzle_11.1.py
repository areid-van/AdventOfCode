with open('input/11.txt') as f:
    stones = [int(x) for x in f.read().split()]

for i in range(25):
    new_stones = list()
    for stone in stones:
        stone_string = str(stone)
        ssl = len(stone_string)
        if stone == 0:
            new_stones.append(1)
        elif (ssl%2) == 0:
            new_stones.append(int(stone_string[0:(ssl//2)]))
            new_stones.append(int(stone_string[(ssl//2):]))
        else:
            new_stones.append(stone*2024)
    stones = new_stones

print('Answer: ', len(stones))
