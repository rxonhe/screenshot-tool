from abc import ABC, abstractmethod


class EventBindable(ABC):
    @abstractmethod
    def event_bind(self, event):
        ...
