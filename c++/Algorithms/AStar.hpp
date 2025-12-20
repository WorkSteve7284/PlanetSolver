#pragma once

#include "Galaxy.hpp"
#include "Path.hpp"
#include <vector>
namespace Algorithms {

    std::vector<Paths::Segment> a_star(planet_index start, planet_index end, const GalaxyMap& map);

}