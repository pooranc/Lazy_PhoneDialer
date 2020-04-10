from lib.keys import Key
from scipy.spatial import distance
import logging

logger = logging.getLogger(__name__)

"""
This class initializes a each digit to specific position, like a standard telephone button layout
        1(0,0)  2(0,1)  3(0,2)
        4(1,0)  5(1,1)  6(1,2)
        7(2,0)  8(2,1)  9(2,2)
        *(3,0)  0(3,1)  #(3,2)
Along with the initial position of the left and right finger which is at "*" and "#" respectively.
and important dial method which populates the tuple.        
"""
class Dialer:
    LEFT_INIT_POS = '*'
    RIGHT_INIT_POS = '#'

    def __init__(self):
        self.positions = {}
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

        self.left_postion = self.LEFT_INIT_POS
        self.right_position = self.RIGHT_INIT_POS

        self.history = [(self.left_postion, self.right_position)]

        self.combined_euclidian_distance = []

    def dial(self, num):
        """
        This method would take single digit of the telephone number and calculate the
        euclidian distance with respect to left and right finger position to digit passed in argument.
        Then based on the the 3 decision populate the tuple of combined euclidian distance and the history of finger movement
        example: (4.0, [('*', '#'), ('1', '#'), ('1', '#'), ('1', '0')]) for Telephone number "110"
        :param num: a single digit of the telephone number
        """
        logger.info(f"Current Position--->({self.left_postion}, {self.right_position})")

        ec_dist_l = self.get_distance(self.left_postion, num)
        logger.info(f"Eucldian distabce w.r.t left finger is: {ec_dist_l}")
        ec_dist_r = self.get_distance(self.right_position, num)
        logger.info(f"Eucldian distabce w.r.t rightfinger is: {ec_dist_r}")

        both_fingers_movement = ec_dist_r + ec_dist_l
        self.combined_euclidian_distance.append(both_fingers_movement)
        logger.info(f"combined euclidian distance: {self.combined_euclidian_distance}")

        if ec_dist_r == ec_dist_l:
            logger.warning("Euclidian distance are eqal, moving left finger by default")
            logger.info(f"Moving  left finger to {num} from self.left_position")
            self.move_left(num)

        if ec_dist_r < ec_dist_l:
            logger.info(f"Moving  right finger to {num} from self.right_position")
            self.move_right(num)
        elif ec_dist_l < ec_dist_r:
            logger.info(f"Moving  left finger to {num} from self.left_position")
            self.move_left(num)

        logger.info(f"Updated Position--->({self.left_postion}, {self.right_position})")

        self.history.append((self.left_postion, self.right_position))
        logger.info(f"Dial History------->{self.history}\n\n\n")

    def get_distance(self, pos, new_pos):
        """
        This method gets the position of the finger digit and new digit position
        and calculates the euclidian distance.
        :param pos: current finger digit
        :param new_pos: new digit
        :return: euclidian distance of two positions
        """
        cur = self.positions[pos].cord()
        new = self.positions[new_pos].cord()
        return distance.euclidean(cur, new)

    def move_right(self, num):
        """
        Updating the right finger position
        :param num: New postion the right finger need to dial
        """
        self.right_position = num

    def move_left(self, num):
        """
        Updating the left finger position
        :param num: New postion the left finger need to dial
        """
        self.left_postion = num

    def get_min_distance(self):
        """
        This method Takes the minmum distance and rounds into integer
        """
        return round(min(self.combined_euclidian_distance))

    def get_history(self):
        return self.history
