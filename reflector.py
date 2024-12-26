class Reflector:
    """
    Reflector in the Enigma machine.
    """
    def __init__(self, wiring):
        self.wiring = wiring  # String: reflector wiring

    def reflect(self, letter):
        index = ord(letter) - ord('A')
        return self.wiring[index]
