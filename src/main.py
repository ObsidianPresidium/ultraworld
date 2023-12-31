import sys
import os
from backend_functions import getch, option_menu
import platform
from create_save import create_save
from environment import environments, get_environment_by_name


if platform.system() == "Windows":
    uw_directory = os.getenv("APPDATA") + "/Ultraworld"
    os.mkdir(uw_directory)
else:
    uw_directory = os.path.expanduser("~/.local/share/Ultraworld")
    os.makedirs(uw_directory, exist_ok=True)

print("Welcome to Ultraworld!")
print("  [N]ew Game")
print("  [L]oad Game")
savegame = option_menu({
    "n": lambda: create_save(uw_directory),
    "l": lambda: print("Thanks for playing!")
})

while True:
    scene = get_environment_by_name(savegame["scene"])
    scene.blurb()
    option_menu(scene.actions)