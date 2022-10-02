def main():
    choice = input('кодируем/декодируем?: ')
    return encode_to_morse() if choice == 'кодируем' else decode_from_morse()


def encode_to_morse():
    text = input().upper().replace(' ', '-').split()
    for word in text:
        print(" ".join([MorseCode_enSimbols[simbol] for simbol in word]), end='', sep=' ')



def decode_from_morse():
    code = input().split()
    for en, morze in MorseCode_enSimbols.items():
        reversedMorseCode_enSimbols[morze] = en
    for part in code:
        print("".join(reversedMorseCode_enSimbols[part]), end='', sep=' ')


MorseCode_enSimbols = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
reversedMorseCode_enSimbols = {}
main()

#.... . .-.. .-.. --- -....- .-- --- .-. .-.. -..