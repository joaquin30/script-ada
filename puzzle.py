from random import randrange

class Board:
    def __init__(self, n):
        self.b = []
        self.n = n
        self.pos = (n-1, n-1)
        for i in range(n):
            l = []
            for j in range(n):
                l.append((i*n + j + 1) % (n*n))
            self.b.append(l)
    
    def __len__(self):
        return self.n

    def __str__(self):
        s = ''
        for l in self.b:
            for i in l:
                if i == 0:
                    s += '#\t'
                else:
                    s += str(i) + '\t'
            s += '\n'
        return s

    def shuffle(self, iterations=100):
        def up(x, y):
            if y > 0:
                self.b[x][y], self.b[x][y-1] = self.b[x][y-1], self.b[x][y]
                y -= 1
            return x, y

        def down(x, y):
            if y < self.n-1:
                self.b[x][y], self.b[x][y+1] = self.b[x][y+1], self.b[x][y]
                y += 1
            return x, y

        def left(x, y):
            if x > 0:
                self.b[x][y], self.b[x-1][y] = self.b[x-1][y], self.b[x][y]
                x -= 1
            return x, y

        def right(x, y):
            if x < self.n-1:
                self.b[x][y], self.b[x+1][y] = self.b[x+1][y], self.b[x][y]
                x += 1
            return x, y

        fn = [up, down, left, right]
        prev = -1
        for _ in range(iterations):
            while True:
                r = randrange(4)
                if r == prev:
                    continue
                p = fn[r](self.pos[0], self.pos[1])
                if p != self.pos:
                    self.pos = p
                    if r == 0:
                        prev = 1
                    elif r == 1:
                        prev = 0
                    elif r == 2:
                        prev = 3
                    elif r == 3:
                        prev = 2
                    break

if __name__ == '__main__':
    from sys import argv
    board = Board(int(argv[1]))
    if len(argv) < 3:
        board.shuffle()    
    else:
        board.shuffle(iterations=int(argv[2]))
    print(board)
