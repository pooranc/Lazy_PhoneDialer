from lib.dialer import Dialer

"""
simple class to pass single digit from the telephone number.
"""
def compute_laziest_path(number):
    """
    Takes in a telephone number, and passes signel digit to dial method of the dialer.py
    :param number: Telephone number
    :return: A tuple, of euclidan distance and the finger movement.
    """
    dr = Dialer()

    for num in number:
        dr.dial(num)

    return (dr.get_min_distance(), dr.get_history())