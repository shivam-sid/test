# File: operations/text_converters.py

def to_binary(input_string: str) -> tuple[bool, str]:
    """Encodes a standard string to a binary string."""
    try:
        binary_string = ' '.join(format(ord(char), '08b') for char in input_string)
        return True, binary_string
    except Exception as e:
        return False, f"Failed to convert to Binary: {e}"

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

MORSE_CODE_REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
# File: operations/text_converters.py

def to_morse(input_string: str) -> tuple[bool, str]:
    """Encodes a standard string to Morse code."""
    try:
        morse_string = ''
        for char in input_string.upper():
            if char in MORSE_CODE_DICT:
                morse_string += MORSE_CODE_DICT[char] + ' '
            elif char == ' ':
                morse_string += '  '  # Two spaces for a word break
            # All other characters, including newlines, will be ignored.
        return True, morse_string.strip()
    except Exception as e:
        return False, f"Failed to convert to Morse: {e}"
    
def from_binary(input_string: str) -> tuple[bool, str]:
    """Decodes a binary string back to a standard string."""
    try:
        # Remove spaces and check for invalid characters
        cleaned_string = input_string.replace(" ", "")
        if not all(c in '01' for c in cleaned_string):
            return False, "Invalid Binary string: contains non-binary characters."
        
        # Binary strings must be multiples of 8
        if len(cleaned_string) % 8 != 0:
            return False, "Invalid Binary string: length is not a multiple of 8."
            
        decoded_string = "".join(chr(int(cleaned_string[i:i+8], 2)) for i in range(0, len(cleaned_string), 8))
        return True, decoded_string
    except Exception as e:
        return False, f"Failed to convert from Binary: {e}"

# File: operations/text_converters.py

# ... (existing functions)

def from_morse(input_string: str) -> tuple[bool, str]:
    """Decodes a Morse code string back to a standard string."""
    try:
        # Split by any whitespace and filter out empty codes
        morse_codes = [code for code in input_string.split() if code]
        
        decoded_string = ""
        for code in morse_codes:
            if code in MORSE_CODE_REVERSE_DICT:
                decoded_string += MORSE_CODE_REVERSE_DICT[code]
            else:
                return False, f"Failed to convert from Morse: Unsupported code '{code}'"
        return True, decoded_string
    except Exception as e:
        return False, f"Failed to convert from Morse: {e}"