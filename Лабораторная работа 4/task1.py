# TODO решите задачу
import json

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME) as f:
        data = json.load(f)
        f.close()
    return sum([round(_dict["score"] * _dict["weight"], 3) for _dict in data])


print(task())
