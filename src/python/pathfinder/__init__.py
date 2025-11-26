""" Implement various algorithms for path finding """

from src import ship, galaxy

from . import check_all
from . import check_manual

def find_path(galaxy_map: galaxy.Galaxy):
    """ Find the most optimal path possible """
    return check_all.find_path(galaxy_map)
