from decorators.action_listener import action_listener
from model.event_bindable import EventBindable


class Mouse(EventBindable):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.actions = {
            "print": False
        }

    @action_listener
    def event_bind(self, event):
        self.x = event.x
        self.y = event.y

    def print(self):
        print("Mouse coordinates X: %d, Y: %d" % (self.x, self.y))
