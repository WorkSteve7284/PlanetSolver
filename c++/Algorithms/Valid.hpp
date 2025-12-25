#pragma once

#include "Galaxy.hpp"
#include "definitions.hpp"
#include <vector>
namespace Algorithms {

    struct Graph {

        std::vector<std::vector<planet_index>> possible_graph;

        Graph(const GalaxyMap&);
    };

}