from entity import Hero
from entity import entities_list
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

    save_game = {
        "player": new_hero.get_attributes_as_dict(),
        "scene": "cave00"
    }
    json_dict = json.dumps(save_game, indent=4)
    with open(uw_directory + "/savegame.json", "w") as file:
        file.write(json_dict)

    return save_game