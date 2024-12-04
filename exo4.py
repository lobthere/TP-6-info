"""
question 1
"""

f = open("notes.txt", "r")

for li in f:
    li = li.strip("\n")

f.close()
