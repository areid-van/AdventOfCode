with open('input/11.txt') as f:
    stones = [int(x) for x in f.read().split()]

cache = {}

def solve(stone, N):
    if(N == 0):
        return(1)

    k = (stone, N)
    if k in cache:
        return cache[k]

    stone_string = str(stone)
    ssl = len(stone_string)
    if stone == 0:
        x = solve(1, N-1)
    elif (ssl%2) == 0:
        s1 = int(stone_string[0:(ssl//2)])
        s2 = int(stone_string[(ssl//2):])
        x = solve(s1, N-1) + solve(s2, N-1)
    else:
        x = solve(stone*2024, N-1)

    cache[k] = x
    return(x)

ans = sum([solve(stone, 75) for stone in stones])
print('Answer: ', ans)
