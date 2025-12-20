#pragma once

#include "Galaxy.hpp"
#include "Path.hpp"
#include "Algorithms/AStar.hpp"
#include "definitions.hpp"
#include <vector>



namespace Algorithms {

    // Wrapper function for actual algorithm
    inline std::vector<Paths::Segment> best_path(planet_index start, planet_index end, const GalaxyMap& map) {
        return a_star(start, end, map);
    }

}