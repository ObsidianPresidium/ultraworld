from entity import Hero
from varname import nameof
import json


def get_name():
    print("What should the hero be called?")
    name = input(": ")
    if name == "":
        name = get_name()

    name = name.title()
    return name


def create_save(uw_directory):
    new_hero = Hero()
    new_hero.name = get_name()

    json_dict = json.dumps(new_hero.get_attributes_as_dict(), indent=4)
    with open(uw_directory + "/player.json", "w") as file:
        file.write(json_dict)

