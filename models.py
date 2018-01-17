from .utils import camel_to_snake

class Model:
    def __init__(self, **kwargs):
        print(kwargs)
        for k, v in kwargs.items():
            setattr(self, camel_to_snake(k), v)


class Proposals(Model):
    def __init__(self, client, **kwargs):
        super().__init__(**kwargs)
        self._client = client
        self.user_position = (self.user_position['Lat'], self.user_position['Lon'])
        self.vehicles = [Vehicle(self._client, **v) for v in self.vehicles]

    def __repr__(self):
        return '<Proposals user_position={}, vehicles=<{} Vehicles>>'.format(self.user_position, len(self.vehicles))

class Vehicle(Model):
    def __init__(self, client, **kwargs):
        super().__init__(**kwargs)
        self._client = client
        self.position = (self.position['Lat'], self.position['Long'])

    def __repr__(self):
        return '<Vehicle id="{}", position={}>'.format(self.id, self.position)
