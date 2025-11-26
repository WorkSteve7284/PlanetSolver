""" Given a path, find the best speed for all segments """

from src import basic, ship

def find_speeds(path: list[basic.TravelPath]) -> basic.FinalPath:
    """

    system of eqs:
    score = time - (fuel + o2 + food)
    time = d1 / s1 + d2 / s2 + d3 / s3 ...

    o2 = max - kl * (time since last resupply)
    food = max - kl * (time since last resupply)

    fuel = max - kf * (d1 * s1^2 + d2 * s2^2 + d3 * s3^2)



    """
    return basic.FinalPath([basic.PathSegment(("no", "no"), 100)])
