from lib.keys import Key
from scipy.spatial import distance

"""
  1(0,0)  2(0,1)  3(0,2)
  4(1,0)  5(1,1)  6(1,2)
  7(2,0)  8(2,1)  9(2,2)
  *(3,0)  0(3,1)  #(3,2)
"""


class Dialer:

    def __init__(self):
        self.positions = {}
        self.numbers = "0123456789*#"
        self.positions['0'] = Key(3, 1)
        self.positions['1'] = Key(0, 0)
        self.positions['2'] = Key(0, 1)
        self.positions['3'] = Key(0, 2)
        self.positions['4'] = Key(1, 0)
        self.positions['5'] = Key(1, 1)
        self.positions['6'] = Key(1, 2)
        self.positions['7'] = Key(2, 0)
        self.positions['8'] = Key(2, 1)
        self.positions['9'] = Key(2, 2)
        self.positions['*'] = Key(3, 0)
        self.positions['#'] = Key(3, 2)

        self.left_postion = '*'
        self.right_position = '#'
        self.history = [(self.left_postion, self.right_position)]
        self.combined_euclidian_distance = []

    def dial(self, num):

        ec_dist_l = self.get_distance(self.left_postion, num)
        ec_dist_r = self.get_distance(self.right_position, num)

        both_fingers_movement = ec_dist_r + ec_dist_l
        self.combined_euclidian_distance.append(both_fingers_movement)

        if ec_dist_r == ec_dist_l:
            self.move_left(num)

        if ec_dist_r < ec_dist_l:
            self.move_right(num)
            dist = ec_dist_r
        elif ec_dist_l < ec_dist_r:
            self.move_left(num)
            dist = ec_dist_l

        self.history.append((self.left_postion, self.right_position))

    def get_distance(self, pos, new_pos):
        cur = self.positions[pos].cord()
        new = self.positions[new_pos].cord()
        dist = distance.euclidean(cur, new)
        return dist

    def move_right(self, num):
        self.right_position = num

    def move_left(self, num):
        self.left_postion = num

    def get_min_distance(self):
        return round(min(self.combined_euclidian_distance))

    def get_history(self):
        return self.history