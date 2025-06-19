def number(plate):
    if len(plate) != 6:
        return "No"
    if not plate[0].isupper():
        return "No"
    for i in range(1, 4):
        if not plate[i].isdigit():
            return "No"
    for i in range(4, 6):
        if not plate[i].isupper():
            return "No"
    return "Yes"
plate = input().strip()
print(number(plate))
