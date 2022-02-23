class Caller:
    def __init__(self, city):
        self.city = city

    def prepare_url(self):
        return f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid=5f29851b0fc134375546255d649d924a"
