class Plugboard:
    """
    Plugboard allows letter substitution before and after rotor processing.
    """
    def __init__(self, connections):
        """connections: List of letter pairs (e.g., [("A", "B"), ("C", "D")])"""
        self.mapping = {letter: letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        for a, b in connections:
            self.mapping[a] = b
            self.mapping[b] = a

    def swap(self, letter):
        return self.mapping[letter]