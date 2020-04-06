from lib.dialer import Dialer


def compute_laziest_path(number):
    dr = Dialer()

    for num in number:
        dr.dial(num)

    return (dr.get_min_distance(), dr.get_history())