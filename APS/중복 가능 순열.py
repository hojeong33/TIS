# N자리 M진수 만들기
# 3자리 4진수 만들기 ex) 000 001 002 003 ... 333

#완전 탐색
n=int(input())
m=int(input())
data=[0]*n # 자리수 크기의 리스트 만들어주기

def recur(cur):
    if cur==n:
        print(data)
        return
    for i in range(m):
        data[cur]=i
        recur(cur+1)
recur(0)

# [0, 0, 0]
# [0, 0, 1]
# [0, 0, 2]
# [0, 0, 3]
# [0, 1, 0]
# [0, 1, 1]
# [0, 1, 2]
# [0, 1, 3]
# [0, 2, 0]
# [0, 2, 1]
# [0, 2, 2]
# [0, 2, 3]
# [0, 3, 0]
# [0, 3, 1]
# [0, 3, 2]
# [0, 3, 3]
# [1, 0, 0]
# [1, 0, 1]
# [1, 0, 2]
# [1, 0, 3]
# [1, 1, 0]
# [1, 1, 1]
# [1, 1, 2]
# [1, 1, 3]
# [1, 2, 0]
# [1, 2, 1]
# [1, 2, 2]
# [1, 2, 3]
# [1, 3, 0]
# [1, 3, 1]
# [1, 3, 2]
# [1, 3, 3]
# [2, 0, 0]
# [2, 0, 1]
# [2, 0, 2]
# [2, 0, 3]
# [2, 1, 0]
# [2, 1, 1]
# [2, 1, 2]
# [2, 1, 3]
# [2, 2, 0]
# [2, 2, 1]
# [2, 2, 2]
# [2, 2, 3]
# [2, 3, 0]
# [2, 3, 1]
# [2, 3, 2]
# [2, 3, 3]
# [3, 0, 0]
# [3, 0, 1]
# [3, 0, 2]
# [3, 0, 3]
# [3, 1, 0]
# [3, 1, 1]
# [3, 1, 2]
# [3, 1, 3]
# [3, 2, 0]
# [3, 2, 1]
# [3, 2, 2]
# [3, 2, 3]
# [3, 3, 0]
# [3, 3, 1]
# [3, 3, 2]
# [3, 3, 3]
