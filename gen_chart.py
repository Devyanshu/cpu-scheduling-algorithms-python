# import plotly.graph_objs as go
# import plotly

import json
data = []

'''
data = [
    {'id': 'P1',
        'bt': 4,
        'at': 0,
        'pr': 3,
        'ct': 3
     },
    {'id': 'P2',
        'bt': 9,
        'at': 3,
        'pr': 2,
        'ct': 8
     },
    {'id': 'P3',
        'bt': 7,
        'at': 5,
        'pr': 1,
        'ct': 5
     }
]
'''


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
        tm += " "*(i[0]) + str(i[0])

    print(cht)
    print(tm)


# generate_gantt(data)
