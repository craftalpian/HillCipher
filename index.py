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
                print(f"{pk} x {c} = {pk*c}")
                n += pk*c
            print(f"{'-'*15}+\n{n}\n")
            print(f"> {n} = {n % len(self.character)} mod({len(self.character)})\n")
            r.append(n % len(self.character))
        return r

    def encoding2Chipper(self, string):
        print(f"Original text: {string}")

        string = ''.join(filter(str.isalpha, string.lower()))
        print(f"Get only alphabet: {string.upper()}")

        if len(self.private_key) <= 2:
            # Cek ganjil atau genap
            if len(string) % 2 == 1:
                string += string[-1:]
                print(f"Ooppsss... is even, I add '{string[-1:].upper()}' in last string")

        split_string, r, f = [string[i:i+len(self.private_key)]
                              for i in range(0, len(string), len(self.private_key))], [], ''

        print(f"Split every {len(self.private_key)} character...")

        print("Calculating...\n")
        for a, b in enumerate(split_string):
            r.append(self.matrix(a, b))

        for x in r:
            for i in x:
                print(f"{i} => {self.character[i].upper()}", end=" | ")
                f += self.character[i].upper()
            f += " "

        print(f"\n>>Result: {f}<<")


if __name__ == "__main__":
    chipper = Chipper([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
    chipper.encoding2Chipper("ACT")
