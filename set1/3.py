#Single-byte XOR cipher :
#The hex encoded string has been XOR'd against a single character. Find the key, decrypt the message.

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def SingleCharFreq(s):
    freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0225134,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
  ' ': 0.1918182 
    }
    maxScore = 0
    maxString = ""
    maxKey = '' 
    # Try key from all character in ASCII
    for key in range(0,256):
        # XOR against a char ---> a char is two hex number(256) ---> take two hex number a time
        decString = ""
        decScore = 0
        for i in range(0,len(s),2):
            if i+1 >= len(s) : break
            aChar = int(s[i] + s[i+1] , 16) #turn a char into integer
            decChar = chr(aChar ^ key)
            if decChar.lower() in freqs: # To lower
                decScore += freqs[decChar.lower()]
            decString = decString + decChar
        # If it has a better score
        if decScore > maxScore :
            maxScore = decScore
            maxString = decString
            maxKey = chr(key)
    print("The key is: " + maxKey + " and the decoded string is:")
    print(maxString)

SingleCharFreq(s)