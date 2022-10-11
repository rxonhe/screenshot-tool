from model.mouse import Mouse

_elements = {
    "mouse": Mouse()
}

_bound_entities = {
    "<Motion>": _elements["mouse"]
}


class EventManager:

    def __init__(self, root):
        self.root = root
        self.bind_widgets()

    def bind_widgets(self):
        for event, entity in _bound_entities.items():
            self.root.bind(event, entity.event_bind)

    @staticmethod
    def get_element(key):
        return _elements.get(key)
