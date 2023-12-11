# ElvesLight, always looking to streamline their operations, has decided to implement a new system for 
# tracking the efficiency of their toy assembly lines. Each assembly line is assigned a unique 
# alphanumeric code, consisting of both letters (A-Z) and numbers (0-9). To monitor productivity, 
# they generate a daily report that lists the total number of toys produced by each line.
55872206
# The report, however, uses a unique encryption method to secure the data. 
# The alphanumeric code for each assembly line is transformed using the following steps:

# Convert each letter in the code to its corresponding position in the alphabet (A=1, B=2, ..., Z=26).
# Then find the sum of the first n natural numbers where n number converted from the previous step.
# e.g D = 4, so the sum of the first 4 natural numbers is 10 (1+2+3+4).
# Add these calculated values with the numeric digits in the code.
# Multiply the sum of that by the number of toys produced by that line.
# The final encrypted number is the remainder when this product is divided by 1000.
# For example, consider an assembly line with the code "B4G7" that produced 300 toys. 
# The conversion would be: B (1+2 = 3) + 4 + G (1 + 2 + 3 + 4 + 5 + 6 + 7 = 28) + 7 = 42. Multiply by 300 to get 12600
# The encrypted number is 12600 % 1000 = 6000.

# Your input is given in the following format:
# (Alphanumeric code) (Number of toys produced)
# E.g "B4G7 300"

# Your task is to decrypt the daily production numbers from the encrypted report. 
# Given the alphanumeric codes and their corresponding encrypted numbers, 
# calculate the sum of actual number of toys produced by each assembly line.

inp = """B4G7 182
A5S2 922
J3K4 133""".split("\n")

alphaEncode = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,27)))

ans = 0
for line in inp:
    code, num = line.split()
    num = int(num)
    codeNum = 0
    for char in code:
        if char in alphaEncode:
            codeNum += ((alphaEncode[char])*(alphaEncode[char]+1)) // 2
        else:
            codeNum += int(char)
    ans += (codeNum * num) % 1000
print(ans)
    


