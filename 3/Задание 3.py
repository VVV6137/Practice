def snow(n, k, events):
    snow = [0] * (n + 1)
    results = []
    for event in events:
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

if __name__ == "__main__":
    n, k = map(int, input().split())
    events = [list(map(int, input().split())) for _ in range(k)]
    results = snow(n, k, events)
    for result in results:
        print(result)
