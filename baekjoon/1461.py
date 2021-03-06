n, m = map(int, input().split())
data = list(map(int, input().split()))
pos_data = []
neg_data = []
big_pos = 0
big_neg = 0
group = []
largest = max(max(data), -min(data))
for num in data:
    if num > 0:
        pos_data.append(num)
    else:
        neg_data.append(-1 * num)
pos_data.sort(reverse=True)
neg_data.sort(reverse=True)
for num in range(0, len(pos_data), m):
    small_group = []
    if len(pos_data) - (num + m) >= 0:
        for i in range(m):
            small_group.append(pos_data[num+i])
        group.append(small_group)
    else:
        big_pos = max(pos_data[num:])
for num in range(0, len(neg_data), m):
    small_group = []
    if len(neg_data) - (num + m) >= 0:
        for i in range(m):
            small_group.append(neg_data[num+i])
            # print(neg_data[num+i])
        group.append(small_group)
    else:
        big_neg = max(neg_data[num:])

# print(group)
# print(big_neg)
# print(big_pos)
result = 0
for i in group:
    result += i[0] * 2
result += big_neg * 2
result += big_pos * 2
print(result - largest)
