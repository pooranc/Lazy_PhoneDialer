"""
Simple class to get the position of the keys
"""
class Key:
    def __init__(self, x, y):
        """
        Gets int x and y as the poisiotn of the digit in standard telphone number layout.
        :param x: x co-ordinate of the digit
        :param y: y co-ordinate of the digit
        """
        self.x = x
        self.y = y

    def cord(self):
        """

        :return: return a tuple of the x and y co-ordinate
        """
        return (self.x, self.y)