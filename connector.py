from algorithms import *
import second_screen
import json
algos = {
    '1': first_come_first_serve,
    '2': shortest_job_first,
    '3': shortest_remaining_time,
    '4': priority_preemptive,
    '5': priority_non_preemptive,
    '6': round_robin
}


def main():
    with open('data.json', "r") as read_file:
        data = json.load(read_file)
    f = open('fl.txt')
    txt = next(f)
    txt = txt.strip('\n')
    if txt == '6':
        tq = next(f)
    f.close()
    if txt == '6':
        res = algos[txt](data, int(tq))
    else:
        res = algos[txt](data)
    avg = avg_wt_tat(res)
    data_f = open('data.json', 'w')
    data_f.write(json.dumps(res))
    data_f.close()
    return avg
