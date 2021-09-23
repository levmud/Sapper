from random import randrange
import json
import datetime


class Sapper:
    row, column = 0, 0

    status = int(input('Новая игра(0) или загрузить игру(1): '))
    if status == 0:
        row, column = map(int, input('Введите количество строк и столбцов: ').split())
    else:
        name = input('Введите название: ')

    def set_row(self, val):
        self.row = val

    def set_column(self, val):
        self.column = val

    def get_row(self):
        return self.row

    def get_st(self):
        return self.status

    def get_column(self):
        return self.column

    def get_name(self):
        return self.name

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
            x = randrange(0, self.get_row())
            y = randrange(0, self.get_column())
            if box[x][y] != '*':
                box[x][y] = '*'
                count += 1

    def draw_map(self, map):
        for r in map:
            print(*r)
        print()

    def chek_win(self, map, mines, kol):
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

    def save(self, name, box, visible, now):
        with open(name + '.txt', 'w') as f1:
            json.dump(visible, f1)

        with open(name + '0.txt', 'w') as f2:
            json.dump(self.cod(box), f2)

    def cod(self, box):
        cbox = ''
        for row in box:
            for elem in row:
                if elem == 0:
                    cbox += '0000'
                elif elem == 1:
                    cbox += '0001'
                elif elem == 2:
                    cbox += '0010'
                elif elem == 3:
                    cbox += '0011'
                elif elem == 4:
                    cbox += '0100'
                elif elem == 5:
                    cbox += '0101'
                elif elem == 6:
                    cbox += '0110'
                elif elem == 7:
                    cbox += '0111'
                elif elem == 8:
                    cbox += '1000'
                else:
                    cbox += '1001'
        return cbox

    def decod(self, stcod, col_c, row_c):
        map = [[] * col_c for i in range(row_c)]
        k = 0
        for i in range(0, len(stcod), 4):
            st = stcod[i:i+4]
            if st == '0000':
                elem = 0
            elif st == '0001':
                elem = 1
            elif st == '0010':
                elem = 2
            elif st == '0011':
                elem = 3
            elif st == '0100':
                elem = 4
            elif st == '0101':
                elem = 5
            elif st == '0110':
                elem = 6
            elif st == '0111':
                elem = 7
            elif st == '0100':
                elem = 8
            else:
                elem = '*'
            map[i//4//col_c].append(elem)
        return map








    def __init__(self):
        now = datetime.datetime.now().replace(microsecond=0)
        if self.get_st() == 0:
            box = [[0] * self.get_column() for i in range(self.get_row())]
            visible = [['☐'] * self.get_column() for i in range(self.get_row())]
            mines = randrange((self.get_column() + self.get_row()) // 2 - 2, (self.get_column() + self.get_row()) // 2)
            kol = self.get_column() * self.get_row() - mines - 1

            self.create_bomb(mines, box)

            for row_c in range(0, self.get_row()):
                for col_c in range(0, self.get_column()):
                    if box[row_c][col_c] != '*':
                        self.set_count_bomb(row_c, col_c, box)

        else:
            with open(self.get_name() + '.txt', 'r') as f1:
                visible = json.load(f1)
            self.set_row(len(visible))
            self.set_column(len(visible[0]))
            with open(self.get_name() + '0.txt', 'r') as f2:
                box = json.load(f2)
            box = self.decod(box, self.get_column(), self.get_row())



            mines = 0
            for row in box:
                mines += row.count('*')
            kol = self.get_column() * self.get_row() - mines



        win = False
        loss = False
        pause = False

        self.draw_map(box)

        while not win and not loss and not pause:


            self.draw_map(visible)

            x, y = map(int, input('Введите координаты: ').split())
            act = int(input('Flag(0) или Tap(1) или Save(2): '))

            x -= 1
            y -= 1
            if act == 0:
                visible[x][y] = '!'
            elif act == 1:
                if box[x][y] == '*':
                    loss = True
                else:
                    if box[x][y] == 0:
                        self.clean(x, y, box, visible)
                    else:
                        visible[x][y] = (box[x][y])
            elif act == 2:
                name = input('Введите название: ')
                self.save(name, box, visible, now)
                pause = True
            if self.chek_win(visible, mines, kol):
                win = True

        justnow = datetime.datetime.now().replace(microsecond=0)

        if win:
            with open('games.txt', 'a') as fw:
                fw.write(now.strftime("%d-%m-%Y %H:%M\n"))
                fw.write('%s\n' % ('Время прохождения: ' + str((justnow - now).total_seconds())))
                fw.write('Победа\n')
                for row in box:
                    fw.write('%s\n' % row)
                fw.write('\n')

            print('Победа')
            for r in box:
                print(*r)
        elif loss:
            with open('games.txt', 'a') as fw:
                fw.write(now.strftime("%d-%m-%Y %H:%M\n"))
                fw.write('Поражение\n')
                for row in box:
                    fw.write('%s\n' % row)
                fw.write('\n')
            print('Смерть')
            for r in box:
                print(*r)


game = Sapper()
