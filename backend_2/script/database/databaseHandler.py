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


def get_component(name):
    data = pd.read_csv('Sheet0-Table1.csv',
                       error_bad_lines=False, sep=';', header=0)

    df = pd.DataFrame(data, columns=[
        'CATEGORY_NAME', 'LEVEL_NO', 'PART_NUMBER', 'GENERAL_DESCRIPTION'])

    df.set_index('LEVEL_NO')

    df = df.loc[(df['LEVEL_NO'] == 4)]

    new_list = df.values.tolist()

    ret = []

    for item in new_list:
        if name in item[0].lower():
            ret.append({
                "name": item[2],
                "description": item[3]
            })

    return ret


def get_all_devices():
    data = pd.read_csv('Sheet0-Table1.csv',
                       error_bad_lines=False, sep=';', header=0)

    df = pd.DataFrame(data, columns=[
        'CATEGORY_NAME', 'LEVEL_NO', 'PART_NUMBER', 'GENERAL_DESCRIPTION'])

    df.set_index('LEVEL_NO')

    df = df.loc[(df['LEVEL_NO'] == 4)]

    new_list = df.values.tolist()

    ret = []

    for item in new_list:
        ret.append({
            "name": item[2],
            "description": item[3]
        })

    return ret
