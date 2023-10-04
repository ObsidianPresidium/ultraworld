scene = None
scene_history = []
environments = []
class Environment:
    def __init__(self, name, text):
        self.name = name
        self.default_text = text
        self.actions = {"[M]enu": lambda: switch_scene("menu")}
        self.id = len(environments)
        environments.append(self)

    def blurb(self):
        print(self.default_text)


### ENVIRONMENT FUNCTIONS ###
def get_environment_by_name(name):
    env_dict = {}
    for environment in environments:
        env_dict.update({environment.name: environment})

    return env_dict[name]


def do_nothing():
    pass


def switch_scene(new_scene):
    global scene
    scene_history.append(scene)
    scene = new_scene


### ENVIRONMENTS ###
menu = Environment("menu", "+--- MENU ---+")
menu.actions = {
    "[S]ave Game": lambda: do_nothing(),
    "[Q]uit Game": exit,
    "[B]ack": lambda: switch_scene(len(scene_history) - 1),
}

class Cave00(Environment):
    def __init__(self, name, text):
        super().__init__(name, text)
        self.actions = {"[F]eel Around": self.feel_around}

    def feel_around(self):
        print("You felt around and discovered a torch.")

cave00 = Cave00("cave00", "After a long time asleep, you wake up in a puddle.\nYou are in a dark, wet cave.")
