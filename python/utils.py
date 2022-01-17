class SecretaryInstance(object):
    """docstring for SecretaryInstance."""

    def __init__(self, value, color, type=0):
        super(SecretaryInstance, self).__init__()
        self.value = value
        self.color = color
        self.type = type

    def __str__(self):
        return f"Value: {self.value}, Color: {self.color}, Type: {self.type}"
