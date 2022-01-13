# https://codeforces.com/problemset/problem/734/A

num = int(input())
x = [i for i in input()]

a = 0
d = 0
for w in x:
    if w == "A":
        a += 1
    else:
        d += 1

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")




