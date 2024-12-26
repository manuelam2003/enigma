from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard
from enigma import EnigmaMachine
from analyzer import EnigmaAnalyzer
from analyzer2 import EnigmaAnalyzer2

def main():
    rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch='Q', position=0)
    rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch='A', position=0)
    rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch='V', position=0)
    
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    
    plugboard = Plugboard([("A", "B"), ("C", "D"), ("E", "F")])
    
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)

    message = "HELLO WORLD"
    print("Original Message:", message)
    
    # Save rotor positions before encryption
    original_positions = [rotor.position for rotor in enigma.rotors]
    
    encrypted = enigma.encrypt(message)

    print("Encrypted:", encrypted)

    # Reset Enigma machine rotor positions to original state
    # for i, rotor in enumerate(enigma.rotors):
    #     rotor.position = original_positions[i]
  
    # Use EnigmaAnalyzer with a crib to analyze the message
    # crib = "LD"
    # analyzer = EnigmaAnalyzer2(crib)
    # analyzer.decrypt_with_crib(encrypted, enigma)

if __name__ == "__main__":
    main()
