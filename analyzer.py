class EnigmaAnalyzer:
    """
    Analysis package to decrypt messages using a crib (known plaintext attack).
    """
    def __init__(self, crib):
        self.crib = crib  # Known plaintext fragment

    # def decrypt_with_crib(self, encrypted_message, enigma_machine):
    #     """Attempts to decrypt an encrypted message using a crib."""
    #     for pos in range(len(encrypted_message) - len(self.crib) + 1):
    #         # Adjust Enigma settings and check if crib matches
    #         test_decryption = enigma_machine.encrypt(encrypted_message)
    #         if test_decryption[pos:pos + len(self.crib)] == self.crib:
    #             print(f"Potential match at position {pos}: {test_decryption}")
    #             return test_decryption
    #     print("No match found with the given crib.")
    #     return None

    def decrypt_with_crib(self, encrypted_message, enigma_machine):
      """Attempts to decrypt an encrypted message using a crib."""
      original_positions = [rotor.position for rotor in enigma_machine.rotors]  # Save initial rotor positions
  
      for pos in range(len(encrypted_message) - len(self.crib) + 1):
          # Reset rotor positions before each attempt
          for i, rotor in enumerate(enigma_machine.rotors):
              rotor.position = original_positions[i]
          
          # Attempt decryption
          test_decryption = enigma_machine.encrypt(encrypted_message)
          if test_decryption[pos:pos + len(self.crib)] == self.crib:
              print(f"Potential match at position {pos}: {test_decryption}")
              return test_decryption
  
      print("No match found with the given crib.")
      return None
