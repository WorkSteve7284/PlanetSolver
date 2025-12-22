#pragma once

// Return a list of all possible segments

#include "Galaxy.hpp"
#include "Path.hpp"
#include "Valid.hpp"
#include "definitions.hpp"
#include <vector>
namespace Algorithms {
inline std::vector<Paths::Segment> show_graph(const GalaxyMap& map) {
    Graph graph(map);

    std::vector<Paths::Segment> out;

    for (int i = 0; i < graph.possible_graph.size(); i++) {
        for (auto& to : graph.possible_graph.at(i))
            out.emplace_back(i, to, 1);
    }

    return out;
}
inline std::vector<Paths::Segment> show_graph_for(planet_index planet, const GalaxyMap& map) {
    Graph graph(map);

    std::vector<Paths::Segment> out;

        for (auto& to : graph.possible_graph.at(planet))
            out.emplace_back(planet, to, 1);

    return out;
}

}