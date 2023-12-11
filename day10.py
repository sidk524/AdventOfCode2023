inp = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".split("\n")

for i in range(len(inp)):
    if "S" in inp[i]:
        start = (i, inp[i].index("S"))
    inp[i] = list(inp[i])
    
