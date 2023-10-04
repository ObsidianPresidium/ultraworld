entities = []

class Hero:
    def __init__(self):
        self.id = len(entities)
        self.name = ""
        self.inventory = {}
        entities.append(self)

    def get_attributes_as_dict(self):
        return {
            "name": self.name
        }

def get_entity_by_id(id):
    return entities[id]

def entities_list():
    return entities