class EnigmaMachine:
    """
    Enigma Machine combining rotors, plugboard, and reflector.
    """
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors          # List of Rotor objects
        self.reflector = reflector    # Reflector object
        self.plugboard = plugboard    # Plugboard object

    def encrypt(self, message):
        encrypted_message = []
        for letter in message:
            if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                encrypted_message.append(letter)
                continue

            # print(f"Input letter: {letter}")  # Debugging: Input to encryption process
            
            # Step 1: Plugboard
            letter = self.plugboard.swap(letter)
            # print(f"After plugboard: {letter}")

            # Step 2: Rotors Forward
            for i, rotor in enumerate(self.rotors):
                letter = rotor.encode_forward(letter)
                # print(f"After rotor {i + 1} forward: {letter}")

            # Step 3: Reflector
            letter = self.reflector.reflect(letter)
            # print(f"After reflector: {letter}")

            # Step 4: Rotors Backward
            for i, rotor in enumerate(reversed(self.rotors)):
                letter = rotor.encode_backward(letter)
                # print(f"After rotor {len(self.rotors) - i} backward: {letter}")

            # Step 5: Plugboard
            letter = self.plugboard.swap(letter)
            # print(f"After plugboard (final): {letter}")

            # Step 6: Rotate Rotors
            rotate_next = True
            for i, rotor in enumerate(self.rotors):
                if rotate_next:
                    rotate_next = rotor.rotate()
                    # print(f"Rotor {i + 1} rotated to position: {rotor.position}")
                else:
                    break

            encrypted_message.append(letter)
        return ''.join(encrypted_message)
