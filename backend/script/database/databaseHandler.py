"""
es.
input: mouse
output: tutte le componenti che fanno un mouse

return: 

[
    {
        name: "bla bla"
        description: bla bla bla
    }
]

----> pandas
"""

import pandas as pd
import random

data = pd.read_csv('/script/database/Sheet0-Table1.csv',
                   error_bad_lines=False, sep=';', header=0)

df = pd.DataFrame(data, columns=[
    'CATEGORY_NAME', 'LEVEL_NO', 'PART_NUMBER', 'GENERAL_DESCRIPTION'])


def get_component(name):
    global df

    df = df.loc[(df['LEVEL_NO'] == 4)]

    new_list = df.values.tolist()

    ret = []

    for item in new_list:
        if name.lower() in item[0].lower():
            ret.append({
                "name": item[2],
                "description": item[3]
            })

    return ret


def get_all_devices():
    global df

    df.set_index('LEVEL_NO')

    df = df.loc[(df['LEVEL_NO'] == 4)]

    new_list = df.values.tolist()

    ret = []

    for item in new_list:
        if item[0] not in ret:
            ret.append(item[0])

    return ret


def get_random_components(num, present):
    new_list = df.values.tolist()
    random.shuffle(new_list)
    ret = []
    i = 0
    for item in new_list:
        if i > num:
            break
        to_append = {
                "name": item[2],
                "description": item[3]
            }
        if to_append not in present:
            ret.append(to_append)
            i += 1
    return ret
