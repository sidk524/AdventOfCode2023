inp = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")
cache = {}
def getCombos(s, p):
    
    if s+"".join(list(map(str, p))) in cache:
        return cache[s+"".join(list(map(str, p)))]
    j = [i for i in s.split(".") if i != ""]
    # print(j)
    for n,i in enumerate(j):
        if list(set(i)) == ["#"]:
            if len(i) != p[n]:
                cache[s+"".join(list(map(str, p)))] = 0
                return 0
        else:
            break
    if "?" not in s:
        if [x for x in list(map(len, s.split("."))) if x != 0] == p:
            cache[s+"".join(list(map(str, p)))] = 1
            return 1
        else:
            cache[s+"".join(list(map(str, p)))] = 0
            return 0
    else:
        i = s.index("?")
        x = getCombos(s[:i]+"#"+s[i+1:], p)
        cache[s[:i]+"#"+s[i+1:]+"".join(list(map(str, p)))] = x
        y = getCombos(s[:i]+"."+s[i+1:], p)
        cache[s[:i]+"."+s[i+1:]+"".join(list(map(str, p)))] = y

        return x+y
ans = 0
for line in inp:
    s, p = line.split()
    p = [int(x) for x in p.split(",")]
    s = "?".join([s]*5)
    p = p*5
    ans += getCombos(s, p)

print(ans)
    
        
