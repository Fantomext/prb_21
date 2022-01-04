def split(word):
    word = word.upper()
    return [char for char in word]

def EnterMorze(word):

    print(word)
    for i in range(len(word)):
        for key in d.keys():
            if key == word[i]:
                print(d[key], end = ' ')

def Main():
    
    print("Enter word on English and we convert this in Morse")
    word = input()
    word = split(word)
    EnterMorze(word)

    #куда лучше всего было вставить словарь в какую-нибудь функцию или так оставить? 
d = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

Main()

    


   
    