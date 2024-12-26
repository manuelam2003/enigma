from itertools import permutations

class EnigmaAnalyzer:
    """
    Analysis package to decrypt messages using a crib (known plaintext attack).
    """
    def __init__(self, crib):
        self.crib = crib  # Known plaintext fragment
    
    def decrypt_with_crib(self, encrypted_message, enigma_machine):
        """Attempts to decrypt an encrypted message using a crib and tries every rotor combination."""
        original_positions = [rotor.position for rotor in enigma_machine.rotors]  # Save initial rotor positions
        rotors = enigma_machine.rotors

        # Try every permutation of rotors
        for rotor_order in permutations(rotors):
            # Try every rotor position combination (26^3 for 3 rotors)
            for positions in self.generate_rotor_positions():
                # Reset rotor positions before each attempt
                for i, rotor in enumerate(rotor_order):
                    rotor.position = positions[i]
                
                # Print the rotor order in a human-readable format
                readable_order = [str(rotor) for rotor in rotor_order]
                # print(f"Testing rotor order: {', '.join(readable_order)} with positions {positions}")

                # Attempt decryption
                test_decryption = enigma_machine.encrypt(encrypted_message)
                if test_decryption.find(self.crib) != -1:
                    print(f"Potential match with rotor order {', '.join(readable_order)} and positions {positions}: {test_decryption}")
                    return test_decryption
        
        print("No match found with the given crib.")
        return None


    def generate_rotor_positions(self):
        """Generate all possible positions for the rotors (26^3 for 3 rotors)."""
        for pos1 in range(26):
            for pos2 in range(26):
                for pos3 in range(26):
                    yield (pos1, pos2, pos3)