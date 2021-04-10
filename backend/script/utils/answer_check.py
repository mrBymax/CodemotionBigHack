import json
from database import databaseHandler


def check_answers(file):
    with open(file, 'w') as f:
        data = json.load(f)

        flag = {
            "present": "true"
        }

        json_object = json.dumps(flag, f, indent=4, sort_keys=True)
        for d in range(len(data)):
            if(data["data"]["component"] == get_component('ABS')):
                f.write(json_object)


check_answers('backend_2/script/utils/test.json')


# if answer component in lista. se c'è aggiungi il tag present:component in array
