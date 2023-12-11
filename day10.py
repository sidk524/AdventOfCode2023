inp = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".split("\n")

for i in range(len(inp)):
    if "S" in inp[i]:
        start = (i, inp[i].index("S"))
    inp[i] = list(inp[i])
    

d = {"|": "ns", "-": "ew", "L": "ne", "J": "nw", "7": "sw", "F": "se", "S": "se"}

opposite = {"n": "s", "s": "n", "e": "w", "w": "e"}

def checkconnect(a, b):
    if inp[a[0]][a[1]] == "." or inp[b[0]][b[1]] == ".":
        return False
    return len(list(set(d[inp[b[0]][b[1]]][1] + "".join([opposite[x] for x in d[inp[a[0]][a[1]]]])))) >= 1

paths = [tuple(start)]
seen = set()
ans = 0
while True:
    toadd = []
    for n,curr in enumerate(paths):
        connect = 0
        if curr == start:
            t = curr
        else:
            t = curr[-1]
        for y in range(t[0] - 1, t[0] + 2):
            if y == t[0] or y < 0 or y >= len(inp):
                continue
            if checkconnect(t, (y, t[1])):
                connect += 1
                toadd.append((t, (y, t[1])))
                
        
        for x in range(t[1] - 1, t[1] + 2):
            if x == t[1] or x < 0 or x >= len(inp[0]):
                continue
            if checkconnect(t, (t[0], x)):

                toadd.append((t, (t[0], x)))
                connect += 1
        if connect < 2:
            
            for i in range(connect):
                toadd.pop()

            print("Not a path")
        else:
            for x in toadd:
                seen.add(x)
    paths = toadd
    ans += 1
    if len(set(paths)) != len(paths):
        break
print(ans)

  
            

