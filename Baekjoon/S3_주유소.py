N = int(input())
distance = list(map(int, input().split(" ")))
price = list(map(int, input().split(" ")))

current_idx = 0
next_idx = 1
dist_sum = 0
price_sum = 0

while next_idx < len(price):
    dist_sum += distance[next_idx-1]
    if price[current_idx] > price[next_idx]:
        price_sum += dist_sum * price[current_idx]
        dist_sum = 0
        current_idx = next_idx

    next_idx += 1
if next_idx-current_idx != 1:
    price_sum += dist_sum * price[current_idx]
print(price_sum)