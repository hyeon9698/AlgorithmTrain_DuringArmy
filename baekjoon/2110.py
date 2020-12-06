# 이진 탐색
n, c = list(map(int, input().split()))
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
start = array[1] - array[0]
end = array[-1] - array[0]
result = 0
while (start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
