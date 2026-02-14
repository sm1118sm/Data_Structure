class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

table = [
    ('A', ".-"), ('B', "-..."), ('C', "-.-."), ('D', "-.."),
    ('E', "."), ('F', "..-."), ('G', "--."), ('H', "...."),
    ('I', ".."), ('J', ".---"), ('K', "-.-"), ('L', ".-.."),
    ('M', "--"), ('N', "-."), ('O', "---"), ('P', ".--."),
    ('Q', "--.-"), ('R', ".-."), ('S', "..."), ('T', "-"),
    ('U', "..-"), ('V', "...-"), ('W', ".--"), ('X', "-..-"),
    ('Y', "-.--"), ('Z', "--.."), ('0', '-----'), ('1', '.----'), ('2', '..---'), ('3', '...--'),
    ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'),
    ('8', '---..'), ('9', '----.'),
    ('.', '.-.-.-'), (',', '--..--'), ('?', '..--..'), ("'", '.----.'),
    ('!', '-.-.--'), ('/', '-..-.'), ('(', '-.--.'), (')', '-.--.-'),
    ('&', '.-...'), (':', '---...'), (';', '-.-.-.'), ('=', '-...-'),
    ('+', '.-.-.'), ('-', '-....-'), ('_', '..--.-'), ('"', '.-..-.'),
    ('$', '...-..-'), ('@', '.--.-.')
]

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

def make_morse_tree():
    root = TNode(None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left is None:
                    node.left = TNode(None)
                node = node.left
            elif c == '-':
                if node.right is None:
                    node.right = TNode(None)
                node = node.right
        
        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data

morseCodeTree = make_morse_tree()
user_input = input("입력 문장 : ")
morse_list = [encode(ch) for ch in user_input.upper()]

print("Morse Code:", morse_list)
print("Decoding : ", end='')

for code in morse_list:
    ch = decode(morseCodeTree, code)
    print(ch, end='')

print()
