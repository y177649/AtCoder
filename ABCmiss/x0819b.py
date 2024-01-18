month = int(input())
day = list(map(int,input().split()))

half_sum_day = (sum(day)+1) // 2
f_month = 0

day = [sum(day[:f_month + 1]) for f_month in range(month)]

for f_month in range(month):
    if day[f_month] >= half_sum_day:
        print(f_month + 1 , half_sum_day - day[f_month - 1])
        print(half_sum_day)
        print(day[f_month])
        break