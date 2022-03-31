n = int(input())
count = 0
strs = []
exceptions = []

for i in range(n):
    strs.append(input())

final_str = "BSUIROPENX"


def concatenate():
    for i in range(n):
        for j in range(n):
            teststr = strs[i] + strs[j]
            if len(teststr) == 10:
                if teststr == final_str:
                    count += 1
            if len(teststr > 10):
                continue
            if len(teststr < 10):
                for z in range(n):
                    teststr += 1
