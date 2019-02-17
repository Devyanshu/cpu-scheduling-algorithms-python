import json
data = []


def generate_gantt():
    with open('data.json', "r") as read_file:
        data = json.load(read_file)
    lst = []
    for dct in data:
        lst.append([dct['ct'], dct['id']])
    lst.sort()
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + i[1] + i[0]//2*'_' + '|'
        tm += " "*(i[0]+1) + str(i[0])

    print(cht)
    print(tm)


# generate_gantt(data)
