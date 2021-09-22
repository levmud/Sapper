from random import randrange
import json
import datetime


class Sapper:

    # row = 5
    # column = 5
    row, column = map(int, input('Введите количество строк и столбцов: ').split())

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def set_count_bomb(self, row_c, col_c, box):
        if row_c == 0:
            if col_c == 0:
                count = 0
                if box[row_c + 1][col_c] == '*':
                    count += 1
                if box[row_c][col_c + 1] == '*':
                    count += 1
                if box[row_c + 1][col_c + 1] == '*':
                    count += 1
                box[row_c][col_c] = count
            elif col_c == self.get_column() - 1:
                count = 0
                if box[row_c + 1][col_c] == '*':
                    count += 1
                if box[row_c][col_c - 1] == '*':
                    count += 1
                if box[row_c + 1][col_c - 1] == '*':
                    count += 1
                box[row_c][col_c] = count
            else:
                count = 0
                if box[row_c + 1][col_c] == '*':
                    count += 1
                if box[row_c][col_c - 1] == '*':
                    count += 1
                if box[row_c + 1][col_c - 1] == '*':
                    count += 1
                if box[row_c + 1][col_c + 1] == '*':
                    count += 1
                if box[row_c][col_c + 1] == '*':
                    count += 1
                box[row_c][col_c] = count

        elif row_c == self.get_row() - 1:
            if col_c == 0:
                count = 0
                if box[row_c - 1][col_c] == '*':
                    count += 1
                if box[row_c][col_c + 1] == '*':
                    count += 1
                if box[row_c - 1][col_c + 1] == '*':
                    count += 1
                box[row_c][col_c] = count
            elif col_c == self.get_column() - 1:
                count = 0
                if box[row_c - 1][col_c] == '*':
                    count += 1
                if box[row_c][col_c - 1] == '*':
                    count += 1
                if box[row_c - 1][col_c - 1] == '*':
                    count += 1
                box[row_c][col_c] = count
            else:
                count = 0
                if box[row_c][col_c - 1] == '*':
                    count += 1
                if box[row_c - 1][col_c - 1] == '*':
                    count += 1
                if box[row_c - 1][col_c] == '*':
                    count += 1
                if box[row_c - 1][col_c + 1] == '*':
                    count += 1
                if box[row_c][col_c + 1] == '*':
                    count += 1
                box[row_c][col_c] = count
        else:
            if col_c == 0:
                count = 0
                if box[row_c - 1][col_c] == '*':
                    count += 1
                if box[row_c - 1][col_c + 1] == '*':
                    count += 1
                if box[row_c][col_c + 1] == '*':
                    count += 1
                if box[row_c + 1][col_c + 1] == '*':
                    count += 1
                if box[row_c + 1][col_c] == '*':
                    count += 1
                box[row_c][col_c] = count
            elif col_c == self.get_column() - 1:
                count = 0
                if box[row_c - 1][col_c] == '*':
                    count += 1
                if box[row_c - 1][col_c - 1] == '*':
                    count += 1
                if box[row_c][col_c - 1] == '*':
                    count += 1
                if box[row_c + 1][col_c - 1] == '*':
                    count += 1
                if box[row_c + 1][col_c] == '*':
                    count += 1
                box[row_c][col_c] = count
            else:
                count = 0
                if box[row_c - 1][col_c] == '*':
                    count += 1
                if box[row_c - 1][col_c - 1] == '*':
                    count += 1
                if box[row_c][col_c - 1] == '*':
                    count += 1
                if box[row_c + 1][col_c - 1] == '*':
                    count += 1
                if box[row_c + 1][col_c] == '*':
                    count += 1
                if box[row_c + 1][col_c + 1] == '*':
                    count += 1
                if box[row_c][col_c + 1] == '*':
                    count += 1
                if box[row_c - 1][col_c + 1] == '*':
                    count += 1
                box[row_c][col_c] = count

    def clean(self, x, y, box, visible):
        visible[x][y] = box[x][y]
        if box[x][y] == 0:
            if x == 0:
                if y == 0:
                    if visible[x + 1][y] == '☐':
                        self.clean(x + 1, y, box, visible)
                    if visible[x + 1][y + 1] == '☐':
                        self.clean(x + 1, y + 1, box, visible)
                    if visible[x][y + 1] == '☐':
                        self.clean(x, y + 1, box, visible)
                elif y == self.get_column() - 1:
                    if visible[x + 1][y] == '☐':
                        self.clean(x + 1, y, box, visible)
                    if visible[x + 1][y - 1] == '☐':
                        self.clean(x + 1, y - 1, box, visible)
                    if visible[x][y - 1] == '☐':
                        self.clean(x, y - 1, box, visible)
                else:
                    if visible[x][y - 1] == '☐':
                        self.clean(x, y - 1, box, visible)
                    if visible[x + 1][y - 1] == '☐':
                        self.clean(x + 1, y - 1, box, visible)
                    if visible[x + 1][y] == '☐':
                        self.clean(x + 1, y, box, visible)
                    if visible[x + 1][y + 1] == '☐':
                        self.clean(x + 1, y + 1, box, visible)
                    if visible[x][y + 1] == '☐':
                        self.clean(x, y + 1, box, visible)
            elif x == self.get_row() - 1:
                if y == 0:
                    if visible[x - 1][y] == '☐':
                        self.clean(x - 1, y, box, visible)
                    if visible[x - 1][y + 1] == '☐':
                        self.clean(x - 1, y + 1, box, visible)
                    if visible[x][y + 1] == '☐':
                        self.clean(x, y + 1, box, visible)
                elif y == self.get_column() - 1:
                    if box[x - 1][y] == 0 and visible[x - 1][y] == '☐':
                        self.clean(x - 1, y, box, visible)
                    else:
                        visible[x - 1][y] = box[x - 1][y]
                    if visible[x - 1][y - 1] == '☐':
                        self.clean(x - 1, y - 1, box, visible)
                    if visible[x][y - 1] == '☐':
                        self.clean(x, y - 1, box, visible)
                else:
                    if visible[x][y - 1] == '☐':
                        self.clean(x, y - 1, box, visible)
                    if visible[x - 1][y - 1] == '☐':
                        self.clean(x - 1, y - 1, box, visible)
                    if visible[x - 1][y] == '☐':
                        self.clean(x - 1, y, box, visible)
                    if visible[x - 1][y + 1] == '☐':
                        self.clean(x - 1, y + 1, box, visible)
                    if visible[x][y + 1] == '☐':
                        self.clean(x, y + 1, box, visible)
            elif y == 0:
                if visible[x - 1][y] == '☐':
                    self.clean(x - 1, y, box, visible)
                if visible[x - 1][y + 1] == '☐':
                    self.clean(x - 1, y + 1, box, visible)
                if visible[x][y + 1] == '☐':
                    self.clean(x, y + 1, box, visible)
                if visible[x + 1][y + 1] == '☐':
                    self.clean(x + 1, y + 1, box, visible)
                if visible[x + 1][y] == '☐':
                    self.clean(x + 1, y, box, visible)
            elif y == self.get_column() - 1:
                if visible[x - 1][y] == '☐':
                    self.clean(x - 1, y, box, visible)
                if visible[x - 1][y - 1] == '☐':
                    self.clean(x - 1, y - 1, box, visible)
                if visible[x][y - 1] == '☐':
                    self.clean(x, y - 1, box, visible)
                if visible[x + 1][y - 1] == '☐':
                    self.clean(x + 1, y - 1, box, visible)
                if visible[x + 1][y] == '☐':
                    self.clean(x + 1, y, box, visible)
            else:
                if visible[x - 1][y] == '☐':
                    self.clean(x - 1, y, box, visible)
                if visible[x - 1][y + 1] == '☐':
                    self.clean(x - 1, y + 1, box, visible)
                if visible[x][y + 1] == '☐':
                    self.clean(x, y + 1, box, visible)
                if visible[x + 1][y + 1] == '☐':
                    self.clean(x + 1, y + 1, box, visible)
                if visible[x + 1][y] == '☐':
                    self.clean(x + 1, y, box, visible)
                if visible[x + 1][y - 1] == '☐':
                    self.clean(x + 1, y - 1, box, visible)
                if visible[x][y - 1] == '☐':
                    self.clean(x, y - 1, box, visible)
                if visible[x - 1][y - 1] == '☐':
                    self.clean(x - 1, y - 1, box, visible)
        return

    def create_bomb(self, mines, box):
        count = 0
        while count <= mines:
            x = randrange(0, self.get_column())
            y = randrange(0, self.get_row())
            if box[x][y] != '*':
                box[x][y] = '*'
                count += 1

    def draw_map(self,map):
        for r in map:
            print(*r)
        print()
    def chek_win(self,map, mines, kol):
        count = 0
        for row in map:
            count += row.count(0)
            count += row.count(1)
            count += row.count(2)
            count += row.count(3)
            count += row.count(4)
            count += row.count(5)
            count += row.count(6)
            count += row.count(7)
            count += row.count(8)
        if count == kol:
            return True
        else:
            return False



    def __init__(self):
        box = [[0] * self.get_row() for i in range(self.get_column())]
        visible = [['☐'] * self.get_row() for i in range(self.get_column())]
        mines = randrange((self.get_column() + self.get_row()) / 2 - 2, (self.get_column() + self.get_row()) / 2)
        kol = self.get_column() * self.get_row() - mines - 1

        self.create_bomb(mines,box)

        for row_c in range(0, self.get_row()):
            for col_c in range(0, self.get_column()):
                if box[row_c][col_c] != '*':
                    self.set_count_bomb(row_c, col_c, box)
        self.draw_map(box)

        win = False
        loss = False

        while not win and not loss:

            self.draw_map(visible)

            x, y = map(int, input('Введите координаты: ').split())
            act = int(input('Flag(0) или Tap(1): '))

            x -= 1
            y -= 1
            if act == 0:
                visible[x][y] = '!'
            else:
                if box[x][y] == '*':
                    loss = True
                else:
                    if box[x][y] == 0:
                        self.clean(x, y, box, visible)
                    else:
                        visible[x][y] = (box[x][y])

            if self.chek_win(visible,mines,kol):
                win = True

        now = datetime.datetime.now()

        if win:
            with open('file.txt', 'a') as fw:
                # записываем
                # json.dump(box, fw)
                fw.write(now.strftime("%d-%m-%Y %H:%M\n"))
                fw.write('Победа\n')
                for row in box:
                    fw.write('%s\n' % row)
                fw.write('\n')

            print('Победа')
            for r in box:
                print(*r)
        else:
            with open('file.txt', 'a') as fw:
                # записываем
                # json.dump(box, fw)
                fw.write(now.strftime("%d-%m-%Y %H:%M\n"))
                fw.write('Поражение\n')
                for row in box:
                    fw.write('%s\n' % row)
                fw.write('\n')
            print('Смерть')
            for r in box:
                print(*r)


game = Sapper()

