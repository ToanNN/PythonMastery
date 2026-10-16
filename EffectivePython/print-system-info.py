import sys

print(sys.version)
print(sys.platform)
print(sys.implementation.name)
print(sys.version_info)


def get_first_int(values, key, default=0):
    value = values.get(key, [""])

    if value[0]:
        return int(value[0])
    return default


snack_calories = {
    "chips": 140,
    "popcorn": 80,
    "nuts": 190,
}
items = list(snack_calories.items())
print(items)

snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]

for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]

    print(f"#{i+1}: {name} has {calories} calories")

for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} calories")

i = 3

x = "even" if i % 2 == 0 else "odd"
print(x)


## Loop and a half
def pick_fruit():
    return {"mango": 20, "banana": 200, "strawberry": 30}


def make_juice(fruit, count):
    return f"{count} bottles of {fruit}"


bottles = []

# walrus operator :=  check if fresh_fruit is not empty
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)


## Use Match


def take_action(light):
    match light:
        case "red":
            print("Stop")
        case "blue":
            print("Go")
        case "green":
            print("Go")
        case "yellow":
            print("Slow down")


## Use enum

import enum

class ColorEnum(enum.Enum):
    RED ="red"
    YELLOW="yellow"
    GREEN ="green"


def take_anotheraction(light):
    match light:
        case ColorEnum.RED:
            print("Stop")
        case ColorEnum.YELLOW:  # Changed
            print("Slow down")
        case ColorEnum.GREEN:  # Changed
            print("Go!")
        case _:
            raise RuntimeError


