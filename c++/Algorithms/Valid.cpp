#include "Valid.hpp"
#include "Galaxy.hpp"
#include <iostream>
#include <vector>

Algorithms::Graph::Graph(const GalaxyMap& map) {
    graph.resize(map.planets.size());

    for (planet_index i = 0; i < map.planets.size(); i++) {

        // Ensure planet isn't hostile
        if (map[i].is_hostile)
            continue;

        const Vector2& A = map[i].pos;

        for (planet_index j = i+1; j < map.planets.size(); j++) {

            // Also ensure planet isn't hostile
            if (map[j].is_hostile)
                continue;

            const Vector2& B = map[j].pos;

            // Check if the segment intersects with a hostile zone
            for (const auto* hostile : map.hostile) {
                const Vector2& C = hostile->pos;
                const Vector2 D = (C - A).project(B - A) + A;

                // If D is between A and B, and it is within the hostile radius
                if (std::min(A.x, B.x) <= D.x && D.x <= std::max(A.x, B.x))
                    if ((C - D).sqr_magnitude() <= hostile->hostile_radius * hostile->hostile_radius)
                        goto fail;
            }

            graph[i].emplace_back(j);
            graph[j].emplace_back(i);

            fail: ;
        }
    }
}

const std::vector<planet_index>& Algorithms::Graph::operator[](planet_index index) const {
    return graph.at(index);
}

void Algorithms::Graph::print() const {

    for (auto& vec : graph) {
        std::string print_vec = "                ";
        for (auto& planet : vec)
            print_vec.at(planet) = 'X';
        std::cout << print_vec << std::endl;
    }

}