class Chipper:
    def __init__(self, private_key):
        self.character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                          "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.private_key = private_key

    def matrix(self, position, target):
        n = len(self.private_key)
        m = target*n
        r, d = [], [list(m[i:i+n]) for i in range(0, len(m), n)]
        for a, b in enumerate(d):
            n = 0
            for i, j in enumerate(b):
                pk, c = self.private_key[a][i], self.character.index(j)
                n += pk*c
            r.append(n % len(self.character))
        return r

    def encoding2Chipper(self, string):
        string = ''.join(filter(str.isalpha, string.lower()))

        m = len(string) % len(self.private_key)
        if m != 0:
            for i in range(m):
                string += string[-1:]

        split_string, r, f = [string[i:i+len(self.private_key)]
                              for i in range(0, len(string), len(self.private_key))], [], ''

        for a, b in enumerate(split_string):
            r.append(self.matrix(a, b))

        for x in r:
            for i in x:
                f += self.character[i].upper()
            f += " "

        return f


if __name__ == "__main__":
    chipper = Chipper([[1, 3], [2, 1]])
    print(chipper.encoding2Chipper("DARK NIGHT"))
