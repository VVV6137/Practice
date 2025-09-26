def snow(n, k, e):
    snow = [0] * (n + 1)
    results = []
    for event in e:
        event_type = event[0]
        if event_type == 1:
            street_index = event[1]
            snow_amount = event[2]
            snow[street_index] += snow_amount
        elif event_type == 2:
            start_index = event[1]
            end_index = event[2]
            total_snow = sum(snow[start_index:end_index + 1])
            results.append(total_snow)
    return results

l = input().split()
n = int(l[0])
k = int(l[1])
e = []
for _ in range(k):
    l = input().split()
    l = list(map(int,l))
    e.append(l)
results = snow(n, k, e)
for i in results:
    print(i)

