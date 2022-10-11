def action_listener(function):
    def wrapper(self, *args, **kwargs):
        for action, do in self.actions.items():
            if do:
                func = getattr(self.__class__, action)
                func(self)
        return function(self, *args, **kwargs)

    return wrapper
