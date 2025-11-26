""" Check only a defined path """

from src import galaxy, ship, basic

def find_path(galaxy_map: galaxy.Galaxy) -> ship.Ship:
    """ Manually check a path """
    my_ship = ship.Ship()

    PATH = ['Luna', 'Mars', 'Juno', 'Titan', 'Echo', 'Xenon', 'Target']
    for target in PATH:

        status = my_ship.goto(galaxy_map, target)

        if status == basic.Status.FAIL:
            print(f"Ship failed while going to {target}!")
            print(f"Resources were {my_ship.resources}")
            print(f"Min & max speeds were min={my_ship.history}")
        else:
            print(f"Ship succeeded while going to {target}!")

    print(f"{my_ship.history[-1]}")
    print(f"{my_ship.resources}")

    return my_ship