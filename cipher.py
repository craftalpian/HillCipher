import math

class Cipher:
    def __init__(self, private_key):
        self.character = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                          "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]
        self.private_key = private_key if isinstance(private_key, list) else self.privateKey2Matrix(private_key)

    def privateKey2Matrix(self, private_key):
        d, b = int(math.sqrt(len(private_key))), []
        for x in list(private_key.lower()):
            b.append(self.character.index(x))
        # https://stackoverflow.com/a/47396778
        return [b[(i*len(b))//d:((i+1)*len(b))//d] for i in range(d)]

    def matrix(self, position, target):
        # Get length of private_key
        n = len(self.private_key)
        m = target*n
        r, d = [], [list(m[i:i+n]) for i in range(0, len(m), n)]
        for a, b in enumerate(d):
            n = 0
            for i, j in enumerate(b):
                pk, c = self.private_key[a][i], self.character.index(j)
                print(f"{j} is {c}")
                n += pk*c
            r.append(n % len(self.character))
            print(f"{n} => {n % len(self.character)} [{self.character[n % len(self.character)].upper()}]")
        return r

    def encoding2Cipher(self, string):
        # Remove whitespace and only get alphabet
        string = "".join(filter(str.isalpha, string.lower()))

        # Count mod for append last character in list var
        mod = len(string) % len(self.private_key)
        if mod != 0:
            for i in range(mod):
                string += string[-1:]

        # Split string to adjust dimensional size between matrix and string
        split_string, r, f = [string[i:i+len(self.private_key)]
                              for i in range(0, len(string), len(self.private_key))], [], ''

        for a, b in enumerate(split_string):
            r.append(self.matrix(a, b))

        for x in r:
            for i in x:
                f += self.character[i].upper()
            f += " "
        return f