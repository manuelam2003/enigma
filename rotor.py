class Rotor:
    """
    A single Enigma rotor that shifts characters according to its wiring.
    """
    def __init__(self, wiring, notch, position=0):
        self.wiring = wiring  # String: the internal wiring of the rotor (e.g., "EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        self.notch = notch    # Character: the rotor's turnover notch position (e.g., 'Q')
        self.position = position  # Integer: the rotor's current rotational position
    
    def __str__(self):
        """Return a human-readable string representation of the rotor."""
        return f"Rotor(wiring={self.wiring[:5]}..., notch={self.notch}, position={self.position})"  # Show first 5 characters for brevity

    def encode_forward(self, letter):
        """Encodes the letter in the forward direction."""
        index = (ord(letter) - ord('A') + self.position) % 26
        encoded_letter = self.wiring[index]
        return chr((ord(encoded_letter) - ord('A') - self.position) % 26 + ord('A'))

    def encode_backward(self, letter):
        """Encodes the letter in the backward direction (reverse signal)."""
        shifted_letter = chr((ord(letter) - ord('A') + self.position) % 26 + ord('A'))
        reverse_index = self.wiring.index(shifted_letter)
        return chr((reverse_index - self.position) % 26 + ord('A'))

    def rotate(self):
        """Rotates the rotor by one position and returns True if the notch is reached."""
        self.position = (self.position + 1) % 26
        return self.position == (ord(self.notch) - ord('A'))
