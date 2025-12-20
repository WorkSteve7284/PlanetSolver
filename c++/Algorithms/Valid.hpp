#pragma once

#include "Galaxy.hpp"
#include "definitions.hpp"
#include <vector>
namespace Algorithms {

    struct Graph {

        std::vector<std::vector<planet_index>> graph;

        Graph(const GalaxyMap&);

        const std::vector<planet_index>& operator[](planet_index) const;

        void print() const;
    };

}